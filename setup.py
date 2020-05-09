"""setup.py"""
from setuptools import setup, find_packages

setup(
    name='yaml-pipeline',
    version='0.0.1',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().strip().split("\n"),
)
