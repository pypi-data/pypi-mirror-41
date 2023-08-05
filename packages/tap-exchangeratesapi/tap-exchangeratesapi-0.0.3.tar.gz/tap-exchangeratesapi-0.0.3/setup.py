#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-exchangeratesapi',
      version='0.0.3',
      description='Singer.io tap for extracting currency exchange rate data from the exchangeratesapi.io API',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_exchangeratesapi'],
      install_requires=['singer-python==5.3.3',
                        'backoff==1.3.2',
                        'requests==2.13.0'],
      entry_points='''
          [console_scripts]
          tap-exchangeratesapi=tap_exchangeratesapi:main
      ''',
)
