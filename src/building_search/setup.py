from setuptools import find_packages, setup

setup(
	name='seattle_building_ownership',
	packages=find_packages(include=['geo', 'corp_owners', 'parcel_owners']),
	version='0.1.0',
	description='Python package for finding building owners in Seattle',
	author='Linnea May & Isaac Cowhey',
	license='MIT',
	install_requires=['<pandas>', '<numpy>', '<requests>', '<geopandas>', '<urllib>', '<shapely>', '<matplotlib>', '<bs4>'],
)
