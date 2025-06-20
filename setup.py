import os

from setuptools import setup

setup(
    cffi_modules=[ os.path.join("libxeddsa", "build.py") + ":ffibuilder" ]
)
