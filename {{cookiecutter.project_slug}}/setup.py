"""Setuptools installation script for {{ cookiecutter.project_name }} package."""

from setuptools import setup
import re


# Get contents of README file
with open('README.md') as fh:
	readme_contents = fh.read()


# Read version from root module __init__.py
with open('{{ cookiecutter.package_name }}/__init__.py') as fh:
	init_contents = fh.read()
	version_match = re.search('^__version__ = ["\']([^"\']+)["\']', init_contents, re.M)

	if not version_match:
		raise RuntimeError('Unable to get version string')

	version = version_match.group(1)


requirements = [
]

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']


setup(
	name='{{ cookiecutter.project_slug }}',
	version=version,
	description='{{ cookiecutter.project_short_description }}',
	long_description=readme_contents,
	author='{{ cookiecutter.author }}',
	author_email='{{ cookiecutter.author_email }}',
	url='{{ cookiecutter.project_url }}',
	python_requires='>=3.5',
	install_requires=requirements,
	setup_requires=setup_requirements,
	tests_require=test_requirements,
	include_package_data=True,
	# license='',
	# classifiers='',
	# keywords=[],
	# platforms=[],
	# provides=[],
	# requires=[],
	# obsoletes=[],
)
