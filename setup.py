import os

from setuptools import setup

setup(
    # https://github.com/python-cffi/cffi/issues/55
    cffi_modules=[ os.path.join("libxeddsa", "build.py") + ":ffibuilder" ]
)
