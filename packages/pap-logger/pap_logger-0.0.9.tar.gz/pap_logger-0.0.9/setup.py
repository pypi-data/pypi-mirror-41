# coding=utf-8
import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pap_logger",
    version="0.0.9",
    author="KurisuD",
    author_email="KurisuD@pypi.darnand.net",
    description="A 'prêt-à-porter' logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KurisuD/pap_logger",
    packages=setuptools.find_packages(),
    install_requires=['pathlib', 'pytz'],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Topic :: System :: Logging"
    ],
)