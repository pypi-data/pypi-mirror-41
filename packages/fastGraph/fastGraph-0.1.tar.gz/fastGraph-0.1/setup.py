#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

requirements = [
    'argparse>=1.3',
	'gensim>=3.5.0',
	'numpy>=1.13',
	'scipy>=0.20.0',
	'scikit-learn>=0.20',
	'six>=1.8',
	'psutil>=5.0.0',
	'pandas>=0.23'
]

setup(
    name='fastGraph',
    version='0.1',
    description='A fast and lightweight package designed for Graph Embedding.',
    long_description=readme,
    author='Angus Kung',
    author_email='angusthefrog@gmail.com',
    url='https://github.com/AngusKung/fastGraph',
    packages=[
        'fastGraph',
    ],
    entry_points={'console_scripts': ['fastGraph = fastGraph.__main__:main']},
    package_dir={'fastGraph':
                 'fastGraph'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache-2.0",
    keywords='fastGraph',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ]
)