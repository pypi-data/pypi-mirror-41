#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Snippy - command, solution, reference and code snippet manager.
#  Copyright 2017-2019 Heikki J. Laaksonen  <laaksonen.heikki.j@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""setup: Install Snippy tool."""

import io
import os
from setuptools import setup, find_packages


requires = (
    'pyyaml>=3.12,<4 ; python_version<="3.6"',
    'pyyaml>=3.13,<4 ; python_version>="3.7"'
)
extras_dev = (
    'logging_tree==1.8',
    'openapi2jsonschema==0.8.0'
)
extras_docs = (
    'sphinx==1.8.3',
    'sphinxcontrib-openapi==0.3.2',
    'sphinx_rtd_theme==0.4.2',
    'sphinx-autobuild==0.7.1'
)
extras_server = (
    'falcon==1.4.1',
    'gunicorn==19.9.0',
    'jsonschema==2.6.0',
    'psycopg2-binary==2.7.7'
)
extras_tests = (
    'codecov==2.0.15',
    'flake8==3.5.0',
    'logging_tree==1.8',
    'mock==2.0.0',
    'pprintpp==0.4.0',
    'pyflakes==1.6.0',
    'pylint==1.9.3 ; python_version=="2.7.*"',
    'pylint==2.2.2 ; python_version>"2.7"',
    'pytest==4.1.1',
    'pytest-cov==2.6.1',
    'pytest-mock==1.10.0',
    'pytest-xdist==1.26.0',
    'tox==3.5.3'
)

meta = {}
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'snippy', 'meta.py'), mode='r', encoding='utf-8') as f:
    exec(f.read(), meta)

with io.open('README.rst', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name=meta['__title__'],
    version=meta['__version__'],
    description=meta['__description__'],
    long_description=readme,
    long_description_content_type='text/x-rst',
    author=meta['__author__'],
    author_email=meta['__email__'],
    url=meta['__homepage__'],
    license=meta['__license__'],
    keywords='command solution snippet reference link snippet manager server console',
    packages=find_packages(exclude=['tests', 'tests.testlib']),
    package_dir={'snippy': 'snippy'},
    package_data={
        'snippy': [
            'data/defaults/*',
            'data/storage/*',
            'data/templates/*'
        ]
    },
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=requires,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'snippy = snippy.snip:main'
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Documentation',
        'Topic :: Utilities'
    ],
    extras_require={
        'dev': extras_dev + extras_docs + extras_server + extras_tests,
        'docs': extras_docs,
        'server': extras_server,
        'test': extras_server + extras_tests,
    },
    tests_require=extras_tests,
    test_suite='tests'
)
