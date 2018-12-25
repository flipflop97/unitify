#!/usr/bin/env python

from setuptools import setup

setup(
    name='unitify',
    version='1.0.3',
    description='Replaces all nouns in a text with the word "unit"',
    author='Philip Goto',
    author_email='philip.goto@gmail.com',
    url='https://github.com/flipflop97/unitify',
    license='MIT',
    packages=['unitify'],
    scripts=['bin/unitify'],
    install_requires=[
        'spacy',
    ],
    dependency_links=[
        'https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz#egg=en_core_web_sm-2.0.0',
    ],
)
