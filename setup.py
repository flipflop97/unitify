#!/usr/bin/env python3

from setuptools import setup

setup(
    name='unitify',
    version='1.0.1',
    description='Replaces all nouns in a text with the word "unit"',
    author='Philip Goto',
    author_email='philip.goto@gmail.com',
    url='https://github.com/flipflop97/unitify',
    license='MIT',
    packages=['unitify'],
    entry_points = {
        'console_scripts': [
            'unitify=unitify.__main__:main'
        ]
    }
)
