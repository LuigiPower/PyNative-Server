#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='PyNative',
    version='0.0.3',
    description='PyNative library',
    long_description=readme,
    license=license,
    author='Federico Giuggioloni',
    author_email='federico.giuggioloni@gmail.com',
    url='https://github.com/LuigiPower/PyNative-Server',
    scripts=['samples/pynative_sample'],
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'Flask-Triangle']
)

