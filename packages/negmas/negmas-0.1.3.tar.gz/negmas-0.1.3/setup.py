#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'pytest-runner', 'numpy', 'pandas', 'scipy', 'joblib', 'pytest-runner', 'colorlog', 'py4j'
                , 'dataclasses', 'inflect', 'stringcase', 'pyyaml', 'tabulate', 'progressbar2']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Yasser Mohammad",
    author_email='yasserfarouk@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='A library for situated automated negotiations',
    entry_points={
        'console_scripts': [
            'rungenius=negmas.scripts.rungenius.cli',
            'scml=negmas.scripts.scml.cli',
        ],
    },
    install_requires=setup_requirements,
    license="GNU General Public License v2 (GPLv2)",
    long_description=readme,
    include_package_data=True,
    keywords='negmas negotiate negotiation mas multi-agent simulation',
    name='negmas',
    packages=find_packages(include=['negmas']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yasserfarouk/negmas',
    version='0.1.3',
    zip_safe=False,
)
