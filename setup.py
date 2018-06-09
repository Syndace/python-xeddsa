#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "XEdDSA",
    version = "0.1.1",
    description = "A python implementation of the XEdDSA signature scheme.",
    author = "Tim Henkes",
    url = "https://github.com/Syndace/python-xeddsa",
    packages = ["xeddsa", "xeddsa.implementations"],
    requires = ["pynacl"],
    provides = ["xeddsa"]
)
