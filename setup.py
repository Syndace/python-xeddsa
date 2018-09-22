from setuptools import setup, find_packages

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "xeddsa"))

import version

with open("README.md") as f:
    long_description = f.read()

setup(
    name = "XEdDSA",
    # TODO: Don't forget to update the url's in the build.py file after updates to ref10!
    version = version.__version__,
    description = "A python implementation of the XEdDSA signature scheme.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Syndace/python-xeddsa",
    author = "Tim Henkes",
    author_email = "tim@cifg.io",
    license = "MIT",
    packages = find_packages(),
    install_requires = [ "cffi>=1.9.1", "pynacl>=1.0.1" ],
    setup_requires   = [ "cffi>=1.9.1" ],
    cffi_modules     = [ os.path.join("ref10", "build.py") + ":ffibuilder" ],
    python_requires  = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Topic :: Communications :: Chat",
        "Topic :: Security :: Cryptography",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Programming Language :: Python :: Implementation :: CPython",

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
