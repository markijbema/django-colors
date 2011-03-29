#!/usr/bin/env python


import setuptools
from distutils.core import setup
import os, sys

# Dynamically calculate the version based on colors.VERSION.
version = __import__('colors').get_version()
if u'SVN' in version:
    version = ' '.join(version.split(' ')[:-1])

setup(
    name = 'Django Colors',
    version = version.replace(' ', '-'),
    description = 'Manipulate colors with django',
    author = 'Maxime Haineault',
    author_email = 'max@motion-m.ca',
#   cmdclass = cmdclasses,
#   data_files = data_files,
    url = 'http://code.google.com/p/django-colors/',
    packages = ['colors'],
    include_package_data=True,
)

