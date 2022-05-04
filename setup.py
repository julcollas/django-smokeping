#! /usr/bin/env python

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-smokeping',
    version = '0.1',
    packages = ['smokeping'],
    include_package_data = True,
    description = 'Django app for Smokeping configuration.',
    long_description = README,
    author = 'Julien Collas',
    author_email = 'jul.collas@gmail.com',
    install_requires=['django-mptt==0.5.5'],
    classifiers = [
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU License',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ]
)
