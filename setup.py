#!/usr/bin/env python
"""setup.py"""
import os
import io
from setuptools import setup
import rosette

NAME = "rosette_api"
DESCRIPTION = "Babel Street Analytics API Python client SDK"
AUTHOR = "Analytics by Babel Street"
AUTHOR_EMAIL = "analyticssupport@babelstreet.com"
HOMEPAGE = "https://github.com/rosette-api/python"
VERSION = rosette.__version__

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    """read function"""
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as the_file:
            buf.append(the_file.read())
    return sep.join(buf)


LONG_DESCRIPTION = read('README.md')

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license='Apache License',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=['rosette'],
    install_requires=['requests'],
    platforms='any',
    url=HOMEPAGE,
    version=VERSION,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
