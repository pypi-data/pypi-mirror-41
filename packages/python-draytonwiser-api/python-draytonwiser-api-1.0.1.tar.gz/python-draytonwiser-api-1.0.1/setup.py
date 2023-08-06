#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

version = '1.0.1'

setup(name='python-draytonwiser-api',
      version=version,
      description='Python API and command line tool for talking to Drayton Wiser Thermostat',
      url='https://github.com/connor9/python-draytonwiser-api',
      author='David Connor',
      author_email='dconnor@gmail.com',
      license='MIT',
      install_requires=['requests>=2.0'],
      packages=['draytonwiser'],
      zip_safe=True)