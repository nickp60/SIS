"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

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
    version="0.0.4",

    description='genome scaffolder for prokaryotes',
    long_description="""
    a program to generate draft genome sequence scaffolds for prokaryotes.
    https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-13-96
    by Zanoni Dias, Ulisses Dias and João C Setubal
    """,
    url='https://github.com/nickp60/SIS',
    author='Nick Waters',
    author_email='nickp60@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='bioinformatics',
    packages=find_packages(),
    package_data={
       '': [path.join(__name__, "sis", "examples/*")],
    },
    entry_points={
       'console_scripts': [
           'sis.py=scaffoldsis.sis:main',
           'multifasta.py=scaffoldsis.multifasta:main',
       ],
    },
)
