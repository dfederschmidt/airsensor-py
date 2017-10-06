# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='airsensor-py',
    version='0.0.6',
    description='Python package for getting sensor values from an Ambient Air Sensor',
    long_description=readme,
    author='Daniel Federschmidt',
    author_email='daniel@federschmidt.xyz',
    url='https://github.com/dfederschmidt/airsensor-py',
    packages=find_packages(),
    scripts=['bin/airsensor-py']
)