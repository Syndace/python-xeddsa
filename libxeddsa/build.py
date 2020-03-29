from ctypes.util import find_library
import os
import platform
import sys

import cffi

ffibuilder = cffi.FFI()

libxeddsa_dir    = os.path.abspath("libxeddsa")
libxeddsa_header = os.path.join(libxeddsa_dir, "xeddsa.h")

system  = platform.system()
machine = platform.machine()

if not (machine.lower() in [ "amd64", "x86_64" ] and sys.maxsize == 2 ** 63 - 1):
    raise Exception("64 bit operating system and Python installation required.")

libxeddsa_library = None
libsodium_library = None

if find_library("xeddsa") is not None:
    libxeddsa_library = "xeddsa"
    print("Using locally installed version of libxeddsa.")

if libxeddsa_library is None:
    if system == "Linux":
        libxeddsa_library = "xeddsa-linux-amd64"
    if system == "Darwin":
        libxeddsa_library = "xeddsa-macos-amd64"
    if system == "Windows":
        libxeddsa_library = "libxeddsa-windows-amd64"
    print("Using prebuilt version of libxeddsa.")

if system == "Linux":
    libsodium_library = "sodium"
if system == "Darwin":
    libsodium_library = "sodium"
if system == "Windows":
    libsodium_library = "libsodium"

if libxeddsa_library is None or libsodium_library is None:
    raise Exception('Operating system "{}" not supported.'.format(system))

with open(libxeddsa_header) as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    "_libxeddsa",
    '#include "' + libxeddsa_header + '"',
    library_dirs = [ libxeddsa_dir ],
    libraries    = [ libxeddsa_library, libsodium_library ]
)

if __name__ == "__main__":
    ffibuilder.compile()
