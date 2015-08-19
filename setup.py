# -*- coding: utf-8 -*-
"""Installer for the collective.dualresources package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='collective.dualresources',
    version='0.2',
    description="An extension of the plone.resource plone:static zcml directive, that allows to specify two folders for a resource directory registration: A dev-directory and a dist-directory. When plone is running in debug mode the filesystem path specified in dev-directory is used to serve static resources for this resource registration. The dist-directory is used when not in debug mode. This allows to use tools like grunt to build production versions of resources, including minification, concatenation, image minification, etc.",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone',
    author='Sune Broendum Woeller',
    author_email='sune@woeller.dk',
    url='https://github.com/collective/dualresources',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.resource'
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
