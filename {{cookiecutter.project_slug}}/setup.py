"""Setuptools installation script for {{ cookiecutter.project_name }} package.

Most options set in setup.cfg (requires setuptools 30.3 or above).
"""

from setuptools import setup, __version__ as setuptools_v_str


metadata = dict(
	name='{{ cookiecutter.project_slug }}',
	version='{{ cookiecutter.version }}',
	description='{{ cookiecutter.project_short_description }}',
	author='{{ cookiecutter.author }}',
	author_email='{{ cookiecutter.author_email }}',
	url='{{ cookiecutter.project_url }}',

	# classifiers='',
	# license='',
	# keywords=[],
	# platforms=[],
	# provides=[],
	# requires=[],
	# obsoletes=[],
)


# Check setuptools version
setuptools_v = tuple(setuptools_v_str.split('.')[:2])
if setuptools_v < ('30', '3'):
	# Just warn because this isn't the proper way to check at all
	from warnings import warn
	warn(
		"Warning: setuptools version 30.3 is required for installation."
		" This probably won't work."
	)


# Run setup
setup(**metadata)
