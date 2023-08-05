from db_field import *
from tornado import gen
from datetime import datetime
from db_exceptions import ObjectDoesNotExist, MultipleResultFound
from functools import partial
from db_utils import *
from query import Rel, ManyToManyRel, OneToManyRel, ManyToOneRel, RelSet, ManyToManySet, OneToManySet, many2oneGetter, many2oneSetter

TX_SUCCESS = 0
TX_FAIL = 1

class DB_Manager(object):
    select_sql = ''
    insert_sql = ''
    update_sql = ''
    delete_sql = ''

    def __init__(self):
        self._inserts = {}
        self._updates = {}
        self._relationships = {}

    def add_insert(self, attr_name, default=None, auto_now_add=None):
        self._inserts[attr_name] = {'default': default,
                                    'auto_now_add': auto_now_add}

    def add_update(self, attr_name, default=None, auto_now=None):
        self._updates[attr_name] = {'default': default,
                                    'auto_now': auto_now}

    def add_relationship(self, rel_name, relationship):
        if not isinstance(relationship, Rel):
            raise TypeError('add relation_ship fail')
        self._relationships[rel_name] = relationship

    def get_insert_default_val(self, attr_name):
        attr = self._inserts.get(attr_name, None)
        if attr is None:
            return
        default_val = attr.get('default', None)
        if default_val is None:
            auto_now_add = attr.get('auto_now_add', None)
            if auto_now_add:
                default_val = datetime.now()
        return default_val

    def get_update_default_val(self, attr_name):
        attr = self._updates.get(attr_name, None)
        if attr is None:
            return
        default_val = attr.get('default', None)
        if default_val is None:
            auto_now = attr.get('auto_now', None)
            if auto_now:
                default_val = datetime.now()
        return default_val

    def get_relationships(self):
        for rel_name, rel in self._relationships.iteritems():
            yield rel_name, rel

def with_metaclass(meta, *bases):
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temporary_class', (), {})

class ModelMeta(type):
    def __new__(cls, name, bases, attr):
        fields = []
        db_manager = DB_Manager()

        super_new = super(ModelMeta, cls).__new__
        if len(bases) == 0:
            return super_new(cls, name, bases, attr)
        l_name = name.lower()
        o2m_rel_set = set()
        m2m_rel_set = set()

        upper_attr = attr.copy()
        db_connection_pool = get_db_connection_pool(name)
        upper_attr['db_connection_pool'] = db_connection_pool
        for k, v in attr.items():
            if isinstance(v, Field):
                fields.append(k)
                db_manager.add_insert(k, v.default, v.auto_now_add)
                db_manager.add_update(k, v.default, v.auto_now)
                upper_attr.__delitem__(k)
            elif isinstance(v, ManyToOneField):
                _fk = v.foreign_key
                if _fk is None:
                    _fk = k + '_id'
                    v.foreign_key = _fk
                _k = '_' + k
                upper_attr[k] = property(partial(many2oneGetter, outter_param=_k),
                                         partial(many2oneSetter, outter_param=_k, foreign_key=_fk))
                rel_cls = v.to
                fields.append(ManyToOneRel(rel_cls, k, _fk))
                o2m_rel_set.add((rel_cls, _fk))

            elif isinstance(v, ManyToManyField):
                rel_cls = v.to
                mt = v.middle_table
                trf = v.target_rel_field
                srf = v.src_rel_field
                if trf is None:
                    trf = rel_cls.__name__.lower()
                if srf is None:
                    srf = l_name
                db_manager.add_relationship(k, ManyToManyRel(rel_cls, mt, trf, srf))
                rel_attr = k[:k.rfind('_')+1]+l_name+'s'
                m2m_rel_set.add((rel_cls, rel_attr, mt, srf, trf))
                upper_attr.__delitem__(k)

        db_table = attr.get('db_table', None)
        select_sql_field_str = "SELECT `%s`.`id`" % db_table
        insert_sql_field_str = ""
        update_sql_field_str = ""
        for field in fields:
            if isinstance(field, ManyToOneRel):
                f = field.foreign_key
            else:
                f = field
            select_sql_field_str += ',`%s`.`%s`' % (db_table, f)
            insert_sql_field_str += '`%s`,' % f
            update_sql_field_str += '`%s`.`%s`=' % (db_table, f) + '%s,'
        select_sql = select_sql_field_str + " FROM `%s`" % db_table
        insert_sql = "INSERT INTO `%s`(%s) VALUES(%s)" % (db_table, insert_sql_field_str[:-1], '%s,' * (len(fields) - 1) + '%s')
        update_sql = "UPDATE `%s` SET %s WHERE `%s`.`id`=" % (db_table, update_sql_field_str[:-1], db_table) + '%s'

        db_manager.select_sql = select_sql
        db_manager.insert_sql = insert_sql
        db_manager.update_sql = update_sql
        db_manager.delete_sql = 'DELETE FROM `%s` WHERE `%s`.`id`=' % (db_table, db_table) + '%s'

        upper_attr['db_manager'] = db_manager
        upper_attr['fields'] = fields
        new_cls = super_new(cls, name, bases, upper_attr)

        for rel_cls, _fk in o2m_rel_set:
            rel_attr = l_name+'_set'
            rel_cls.db_manager.add_relationship(rel_attr, OneToManyRel(new_cls, _fk, db_connection_pool._kwargs.get('db') != rel_cls.db_connection_pool._kwargs.get('db')))

        for rel_cls, rel_attr, mt, trf, srf in m2m_rel_set:
            rel_cls.db_manager.add_relationship(rel_attr, ManyToManyRel(new_cls, mt, trf, srf))

        return new_cls


class BaseModel(with_metaclass(ModelMeta)):

    db_table = None

    def __init__(self, **kwargs):
        self.id = None
        if self.db_table is None:
            print self.__class__.__name__
            raise ValueError('have not define table name')

        rel_set_num = 0
        for rel_name, rel in self.db_manager.get_relationships():
            if isinstance(rel, OneToManyRel):
                setattr(self, rel_name, OneToManySet(self, rel))
                rel_set_num+=1
            elif isinstance(rel, ManyToManyRel):
                setattr(self, rel_name, ManyToManySet(self, rel))
                rel_set_num+=1
        if rel_set_num > 0:
            self.rel_exec_set = set()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @gen.coroutine
    def execute_tx(self, sql_str, sql_param, tx):
        try:
            ret = yield tx.execute(sql_str, sql_param)
            if self.id is None:
                self.id = ret._result.insert_id
        except Exception as e:
            print e
            yield tx.rollback()
            ret = TX_FAIL
        else:
            ret = TX_SUCCESS
        raise gen.Return(ret)

    @gen.coroutine
    def save(self):
        """
        :return: 0--insertOrUpdate success;1--insertOrUpdate fail
        """
        sql_param = []
        db_manager = self.db_manager
        if self.id is None:
            for f in self.fields:
                if isinstance(f, ManyToOneRel):
                    f = f.foreign_key
                v = getattr(self, f, db_manager.get_insert_default_val(f))
                sql_param.append(v)
            sql_str = db_manager.insert_sql
        else:
            for f in self.fields:
                if isinstance(f, ManyToOneRel):
                    f = f.foreign_key
                v = getattr(self, f, db_manager.get_update_default_val(f))
                sql_param.append(v)
            sql_param.append(self.id)
            sql_str = db_manager.update_sql

        tx = yield self.db_connection_pool.begin()
        ret = yield self.execute_tx(sql_str, sql_param, tx)
        if ret is TX_SUCCESS:
            for rel in self.rel_exec_set:
                if isinstance(rel, RelSet):
                    yield rel.execute(tx)
            self.rel_exec_set.clear()
            yield tx.commit()
        raise gen.Return(ret)

    @gen.coroutine
    def delete(self):
        """
        :return: 0--delete success;1--delete fail
        """
        sql_str = self.db_manager.delete_sql
        sql_param = [self.id]
        tx = yield self.db_connection_pool.begin()
        ret = yield self.execute_tx(sql_str, sql_param, tx)
        if ret is TX_SUCCESS:
            yield tx.commit()
        raise gen.Return(ret)

    @classmethod
    @gen.coroutine
    def filter(cls, group_fields=None, order_fields=None, **where_case):

        select_sql, select_param = get_where_sql(db_table=cls.db_table,
                                                 sql_prefix=cls.db_manager.select_sql, **where_case)

        if group_fields:
            select_sql += 'group by '
            count = len(group_fields)
            for g_case in group_fields:
                select_sql += '%s ' % g_case
                count -= 1
                if count > 0:
                    select_sql += ','
        if order_fields:
            select_sql += 'order by '
            count = len(order_fields)
            for o_field in order_fields:
                if o_field.startswith('-'):
                    select_sql += '%s desc' % o_field[1:]
                else:
                    select_sql += '%s asc' % o_field
                count -= 1
                if count > 0:
                    select_sql += ','
        with (yield cls.db_connection_pool.execute(select_sql, select_param)) as cursor:
            datas = cursor.fetchall()
            query_list = []
            search_fields = cls.fields
            for data in datas:
                ret = cls()
                ret.id = data[0]
                for idx, field in enumerate(search_fields):
                    val = data[idx + 1]
                    if isinstance(field, ManyToOneRel):
                        rel_obj = None
                        if val is not None:
                            try:
                                rel_obj = yield field.rel_cls.get(id=val)
                            except ObjectDoesNotExist:
                                pass
                        setattr(ret, field.rel_name, rel_obj)
                    else:
                        setattr(ret, field, val)
                query_list.append(ret)
        raise gen.Return(query_list)

    @classmethod
    @gen.coroutine
    def all(cls):
        datas = yield cls.filter()
        raise gen.Return(datas)

    @classmethod
    @gen.coroutine
    def get(cls, **where_case):
        select_sql, select_param = get_where_sql(db_table=cls.db_table,
                                                 sql_prefix=cls.db_manager.select_sql,  **where_case)
        with (yield cls.db_connection_pool.execute(select_sql, select_param)) as cursor:
            datas = cursor.fetchall()
            dl = len(datas)
            if dl == 0:
                raise ObjectDoesNotExist
            elif dl > 1:
                raise MultipleResultFound
            else:
                ret = cls()
                data = datas[0]
                ret.id = data[0]
                for idx, field in enumerate(cls.fields):
                    val = data[idx + 1]
                    if isinstance(field, ManyToOneRel):
                        rel_obj = None
                        if val is not None:
                            try:
                                rel_obj = yield field.rel_cls.get(id=val)
                            except ObjectDoesNotExist:
                                pass
                        setattr(ret, field.rel_name, rel_obj)
                    else:
                        setattr(ret, field, val)
                raise gen.Return(ret)