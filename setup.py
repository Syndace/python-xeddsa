#!/usr/bin/env python

from distutils.core import setup

import build_scalarmult_cffi_module
import build_sign_cffi_module

setup(
    name = "XEdDSA",
    version = "0.3.0",
    description = "A python implementation of the XEdDSA signature scheme.",
    author = "Tim Henkes",
    url = "https://github.com/Syndace/python-xeddsa",
    packages = ["xeddsa", "xeddsa.implementations"],
    requires = ["pynacl", "cffi"],
    provides = ["xeddsa"],
    ext_modules = [
        build_scalarmult_cffi_module.ffibuilder.distutils_extension(),
        build_sign_cffi_module.ffibuilder.distutils_extension()
    ]
)
