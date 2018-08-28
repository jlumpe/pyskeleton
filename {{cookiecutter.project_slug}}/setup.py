"""Setuptools installation script for {{ cookiecutter.project_name }} package."""

from setuptools import setup


# Get contents of README file
with open('README.md') as fh:
	readme_contents = fh.read()


requirements = [
]

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']


setup(
	name='{{ cookiecutter.project_slug }}',
	version='{{ cookiecutter.version }}',
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
