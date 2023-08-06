# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='radicale_storage_etesync',
    version='0.2.1',
    author='EteSync',
    author_email='development@etesync.com',
    url='https://github.com/etesync/radicale_storage_etesync',
    description='An EteSync storage plugin for Radicale',
    keywords=['etesync', 'encryption', 'sync', 'pim', 'radicale'],
    license='GPL',
    long_description=open('DESCRIPTION.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'etesync>=0.6.1',
        'Radicale>=2.1.10',
    ]
)
