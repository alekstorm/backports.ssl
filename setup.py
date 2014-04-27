#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Get the version (borrowed from hyper)
version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('backports/ssl/__init__.py', 'r') as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        version = match.group(1)
    else:
        raise RuntimeError('No version number found!')

setup(
    name='backports.ssl',
    version=version,
    description='The Python 3.4 standard `ssl` module API implemented on top of pyOpenSSL',
    long_description=open('README.rst').read(),
    author='Alek Storm',
    author_email='alek.storm@gmail.com',
    url='https://github.com/alekstorm/backports.ssl',
    packages=['backports', 'backports.ssl'],
    package_data={'': ['CONTRIBUTORS.rst', 'LICENSE', 'NOTICES.rst', 'README.rst']},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    extras_requires={'full': ['pyOpenSSL>=0.14', 'pyasn1>=0.1.7']},
)
