from setuptools import setup, find_packages

import os

with open("README.md") as f:
    long_description = f.read()

setup(
    name = "XEdDSA",
    version = "0.3.3", # TODO: Don't forget to update the url's in the build.py file!
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
    python_requires  = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4",
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",

        "Topic :: Communications :: Chat",
        "Topic :: Security :: Cryptography",

        "License :: OSI Approved :: MIT License",

        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows XP",
        "Operating System :: Microsoft :: Windows :: Windows Vista",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 10",

        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",

        "Programming Language :: Python :: Implementation :: CPython",

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
