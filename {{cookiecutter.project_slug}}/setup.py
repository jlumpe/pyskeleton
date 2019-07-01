"""Setuptools installation script for {{ cookiecutter.project_name }} package."""

from setuptools import setup


# Get contents of README file
with open('README.md') as f:
	readme_contents = f.read()


setup(long_description=readme_contents)
