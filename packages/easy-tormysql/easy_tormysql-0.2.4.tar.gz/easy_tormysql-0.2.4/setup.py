import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    install_requires=[
        "tormysql ==0.4.0"
    ],
    name="easy_tormysql",
    version="0.2.4",
    author="NightRaven",
    author_email="1453878150@qq.com",
    description="This module provides a twice encapsulation of TorMySql based on Django's code style.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/encodingForBetterWorld/easy_tormysql",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)