#!/usr/bin/env python

from setuptools import setup, find_packages
import mdc

setup(
  name='mdc',
  version=mdc.__version__,
  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'mdc = mdc.mdc:main'
    ]
  },
  install_requires=[
    'xerox'
  ]
)
