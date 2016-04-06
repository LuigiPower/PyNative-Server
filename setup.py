# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='PyNative',
    version='0.0.1',
    description='PyNative library',
    long_description=readme,
    author='Federico Giuggioloni',
    author_email='federico.giuggioloni@gmail.com',
    url='https://github.com/LuigiPower/PyNative-Server',
    scripts=['samples/pynative_sample'],
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

