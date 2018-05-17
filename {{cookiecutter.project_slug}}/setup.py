"""Setuptools installation script for <package_name> package.

Most options set in setup.cfg (requires setuptools 30.3 or above).
"""

from setuptools import setup, __version__ as setuptools_v_str


metadata = dict(
	name='mypackage',  # UPDATE THIS!
	version='0.1',
	description='',

	author='Jared Lumpe',
	author_email='jared.lumpe@ucsf.edu',
	maintainer='Jared Lumpe',
	maintainer_email='jared.lumpe@ucsf.edu',

	# url='',
	# download_url='',
	# project_urls='',

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
