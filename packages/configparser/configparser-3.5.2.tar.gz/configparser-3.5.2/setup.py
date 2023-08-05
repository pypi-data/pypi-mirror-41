#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This library brings the updated configparser from Python 3.5 to Python 2.6-3.5."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import codecs
import os
import sys
from setuptools import setup, find_packages

readme_filename = os.path.join(os.path.dirname(__file__), 'README.rst')
with codecs.open(readme_filename, encoding='utf8') as ld_file:
    long_description = ld_file.read()

if sys.version_info[0] == 2:
    # bail on UTF-8 and enable `import configparser` for Python 2
    author = 'Lukasz Langa'
    modules = ['configparser']
else:
    author = 'Łukasz Langa'
    modules = []

setup(
    name='configparser',
    version='3.5.2',
    author=author,
    author_email='lukasz@langa.pl',
    maintainer='Jason R. Coombs',
    maintainer_email='jaraco@jaraco.com',
    description=__doc__,
    long_description=long_description,
    url='https://github.com/jaraco/configparser/',
    keywords='configparser ini parsing conf cfg configuration file',
    platforms=['any'],
    py_modules=modules,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    extras_require={':python_version=="2.6"': ['ordereddict']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
