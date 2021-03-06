from setuptools import setup, find_packages

import os
import sys

source_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "xeddsa")

version = {}
with open(os.path.join(source_root, "version.py")) as f:
	exec(f.read(), version)
version = version["__version__"]

project = {}
with open(os.path.join(source_root, "project.py")) as f:
	exec(f.read(), project)
project = project["project"]

with open("README.md") as f:
    long_description = f.read()

classifiers = [
    "Intended Audience :: Developers",

    "License :: OSI Approved :: MIT License",

    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",

    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",

    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy"
]

classifiers.extend(project["categories"])

if version["tag"] == "alpha":
    classifiers.append("Development Status :: 3 - Alpha")

if version["tag"] == "beta":
    classifiers.append("Development Status :: 4 - Beta")

if version["tag"] == "rc":
    classifiers.append("Development Status :: 5 - Production/Stable")

del project["categories"]
del project["year"]

setup(
    version = version["short"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license = "MIT",
    packages = find_packages(),
    install_requires = [ "cffi>=1.12.2,<2", "libnacl>=1.7.1,<=2" ],
    setup_requires   = [ "cffi>=1.12.2,<2" ],
    cffi_modules     = [ os.path.join("ref10", "build.py") + ":ffibuilder" ],
    python_requires  = ">=3.6,<4",
    include_package_data = True,
    zip_safe = False,
    classifiers = classifiers,
    **project
)
