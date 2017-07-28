# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='cloud_utilities',
    version='0.1.0',
    description='Skeleton for python module',
    long_description=readme,
    author='aa',
    author_email='sreeakhila423@gmail.com',
    url='https://github.com/akhila423/quadyster',
    packages=find_packages(exclude=('tests', 'docs'))
)
