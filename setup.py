#!/usr/bin/env python3

# setup module for scaffoldsis, also known as SIS
# Copyright (C) 2017  Zanoni Dias, Ulisses Dias, Nicholas Waters, and João C Setubal
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from setuptools import setup, find_packages
import re
from codecs import open
from os import path
import sys


if sys.version_info <= (3, 0):
    sys.stderr.write("ERROR: SIS requires Python 3 " +
                     "or above...exiting.\n")
    sys.exit(1)

setup(
    name='scaffoldsis',
    version="0.1.0",

    description='genome scaffolder for prokaryotes',
    long_description="""
    a program to generate draft genome sequence scaffolds for prokaryotes.
    https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-13-96
    by Zanoni Dias, Ulisses Dias, Nicholas Waters, and João C Setubal
    """,
    url='https://github.com/nickp60/SIS',
    install_requires=['biopython'],
    author='Nick Waters',
    author_email='nickp60@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 3',
    ],
    keywords='bioinformatics',
    packages=find_packages(),
    package_data={
       '': [path.join(__name__, "examples/*")],
    },
    entry_points={
       'console_scripts': [
           'sis.py=scaffoldsis.sis:main',
           'multifasta.py=scaffoldsis.multifasta:main',
           'scaffold.py=scaffoldsis.scaffold:main',
       ],
    },
)
