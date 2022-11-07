import ctypes.util
import os
import platform
from typing import Optional, Tuple

import cffi  # type: ignore[import]


class LibraryNotFoundException(Exception):
    """
    Raised in case a system library was not found.
    """


def find_library(library: str) -> Tuple[Optional[str], str]:
    """
    Find a system library by name.

    Args:
        library: Name of the system library.

    Returns:
        A tuple, where the first entry contains the path that the library can be found in, and the second
        entry is the name of the library. If `None` is returned for the path, the library is included in the
        necessary search paths to load it without an explicit path.
    """

    names = [ library ]

    if platform.system() == "Windows":
        # Windows library naming convention does not include the `lib` prefix, but some libraries still ship
        # with the prefix.
        names.append(f"lib{library}")

    for name in names:
        library_path = ctypes.util.find_library(name)
        if library_path is not None:
            if os.path.isfile(library_path):
                return os.path.dirname(library_path), name

            return None, name

    raise LibraryNotFoundException(f"Library {name} not found.")


try:
    libxeddsa_dir, libxeddsa_library = find_library("xeddsa")
except LibraryNotFoundException as e:
    raise Exception(
        "No locally installed version of libxeddsa found. Make sure libxeddsa is installed and can be"
        " found by Python/your C compiler."
    ) from e

try:
    libsodium_dir, libsodium_library = find_library("sodium")
except LibraryNotFoundException as e:
    raise Exception(
        "No locally installed version of libsodium found. Make sure libsodium is installed and can be"
        " found by Python/your C compiler."
    ) from e

library_dirs = []
if libxeddsa_dir is not None:
    library_dirs.append(libxeddsa_dir)
if libsodium_dir is not None:
    library_dirs.append(libsodium_dir)

ffibuilder = cffi.FFI()

libxeddsa_header = os.path.join(os.path.dirname(os.path.abspath(__file__)), "xeddsa.h")

with open(libxeddsa_header, encoding="utf-8") as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    "_libxeddsa",
    '#include "' + libxeddsa_header + '"',
    library_dirs=library_dirs,
    libraries=[ libxeddsa_library, libsodium_library ]
)

if __name__ == "__main__":
    ffibuilder.compile()
