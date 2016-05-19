#!/usr/bin/env python

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup_args.update(dict(
    name='lorikeet',
    version="0.1",
    description='Colour and colour mapping for scientific datasets.',
    long_description=open('README.md').read() if os.path.isfile('README.md') else 'Consult README.md',
    platforms=['Windows', 'Mac OS X', 'Linux'],
    license='BSD',
    url='https://github.com/SciTools-incubator/lorikeet',
    package_dir={'': 'lib'},
    packages = ["lorikeet"],
    classifiers = [
        "License :: OSI Approved :: BSD License",
        "Development Status :: 1 - Planning Development Status",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries"]
))

if __name__=="__main__":
    setup(**setup_args)

