import ctypes.util
import os
import platform
import sys
from typing import Optional, Tuple

import cffi # type: ignore[import]

ffibuilder = cffi.FFI()

libxeddsa_prebuilt_dir = os.path.dirname(os.path.abspath(__file__))
libxeddsa_header = os.path.join(libxeddsa_prebuilt_dir, "xeddsa.h")

class LibraryNotFoundException(Exception):
    pass

def find_library(library: str) -> Tuple[Optional[str], str]:
    names = [ library ]

    if platform.system() == "Windows":
        # Windows library naming convention does not include the `lib` prefix, but some library still ship
        # with the prefix.
        names.append("lib{}".format(library))

    for name in names:
        library_path = ctypes.util.find_library(name)
        if library_path is not None:
            if os.path.isfile(library_path):
                return os.path.dirname(library_path), name

            return None, name

    raise LibraryNotFoundException("Library {} not found.".format(name))

def find_libxeddsa() -> Tuple[Optional[str], str]:
    try:
        return find_library("xeddsa")
    except LibraryNotFoundException:
        if os.getenv("LIBXEDDSA_FORCE_LOCAL"):
            raise Exception("No locally installed version of libxeddsa found.")

    print(
        "No locally installed version of libxeddsa found, falling back to prebuilt binaries. Set the"
        " 'LIBXEDDSA_FORCE_LOCAL' environment variable to prevent usage of prebuilt binaries."
    )

    system  = platform.system()
    machine = platform.machine()

    if not (machine.lower() in [ "amd64", "x86_64" ] and sys.maxsize == 2 ** 63 - 1):
        raise Exception(
            "Prebuilt binaries of libxeddsa are not available for the system architecture '{}' and 32 bit"
            " Python interpreters. Build or install libxeddsa and make sure it can be found by Python/your C"
            " compiler."
            .format(machine)
        )

    if system == "Linux":
        return (libxeddsa_prebuilt_dir, "xeddsa-linux-amd64")
    if system == "Darwin":
        return (libxeddsa_prebuilt_dir, "xeddsa-macos-amd64")
    if system == "Windows":
        return (libxeddsa_prebuilt_dir, "libxeddsa-windows-amd64")

    raise Exception(
        "Prebuilt binaries of libxeddsa are not available for operating system '{}'. Build or install"
        " libxeddsa and make sure it can be found by Python/your C compiler."
        .format(system)
    )

def find_libsodium() -> Tuple[Optional[str], str]:
    try:
        return find_library("sodium")
    except LibraryNotFoundException:
        raise Exception(
            "No locally installed version of libsodium found. Make sure libsodium is installed and can be"
            " found by Python/your C compiler."
        )

libxeddsa_dir, libxeddsa_library = find_libxeddsa()
libsodium_dir, libsodium_library = find_libsodium()

library_dirs = []
if libxeddsa_dir is not None:
    library_dirs.append(libxeddsa_dir)
if libsodium_dir is not None:
    library_dirs.append(libsodium_dir)

with open(libxeddsa_header) as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    "_libxeddsa",
    '#include "' + libxeddsa_header + '"',
    library_dirs = library_dirs,
    libraries    = [ libxeddsa_library, libsodium_library ]
)

if __name__ == "__main__":
    ffibuilder.compile()
