#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import dephp as application

try:
    from setuptools import setup
except ImportError:
    print('The installation require distribute, please install it')

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = ["setproctitle", "requests"]

setup(
    name = application.name,
    py_modules = ['dephp'],
    entry_points = {
        'console_scripts': [
            'dephp = dephp:main'
        ],
    },
    install_requires = requires,
    version = application.version,
    description = application.description,
    long_description = README,
    author = "Massimiliano Torromeo",
    author_email = "massimiliano.torromeo@gmail.com",
    url = application.url,
    download_url = "{0}/tarball/v{1}".format(application.url, application.version),
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: BSD",
        "Natural Language :: English",
    ],
    license = "BSD License"
)
