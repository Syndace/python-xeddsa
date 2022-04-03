import ctypes.util
import os
import platform
import sys
from typing import Optional, Tuple

import cffi  # type: ignore[import]

ffibuilder = cffi.FFI()

libxeddsa_prebuilt_dir = os.path.dirname(os.path.abspath(__file__))
libxeddsa_header = os.path.join(libxeddsa_prebuilt_dir, "xeddsa.h")


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


def find_libxeddsa() -> Tuple[Optional[str], str]:
    """
    Find libxeddsa, either a locally installed version, or one of the versions included with the package.

    Returns:
        A tuple, where the first entry contains the path that the library can be found in, and the second
        entry is the name of the library. If `None` is returned for the path, the library is included in the
        necessary search paths to load it without an explicit path.
    """

    try:
        return find_library("xeddsa")
    except LibraryNotFoundException as e:
        if os.getenv("LIBXEDDSA_FORCE_LOCAL"):
            raise Exception("No locally installed version of libxeddsa found.") from e

    print(
        "No locally installed version of libxeddsa found, falling back to prebuilt binaries. Set the"
        " 'LIBXEDDSA_FORCE_LOCAL' environment variable to prevent usage of prebuilt binaries."
    )

    if sys.maxsize != 2 ** 63 - 1:
        raise Exception(
            "Prebuilt binaries of libxeddsa are not available for 32 bit Python interpreters. Build or"
            " install libxeddsa and make sure it can be found by Python/your C compiler."
        )

    system = platform.system()
    machine = platform.machine().lower()

    is_amd64 = machine in { "amd64", "x86_64" }
    is_arm64 = machine in { "arm64" }

    if system == "Linux" and is_amd64:
        return (libxeddsa_prebuilt_dir, "xeddsa-linux-amd64")
    if system == "Darwin" and is_amd64:
        return (libxeddsa_prebuilt_dir, "xeddsa-macos-amd64")
    if system == "Darwin" and is_arm64:
        return (libxeddsa_prebuilt_dir, "xeddsa-macos-arm64")
    if system == "Windows" and is_amd64:
        return (libxeddsa_prebuilt_dir, "libxeddsa-windows-amd64")

    raise Exception(
        f"Prebuilt binaries of libxeddsa are not available for operating system '{system}' on architecture"
        f" '{machine}'. Build or install libxeddsa and make sure it can be found by Python/your C compiler."
    )


def find_libsodium() -> Tuple[Optional[str], str]:
    """
    Find a locally installed version of libsodium.

    Returns:
        A tuple, where the first entry contains the path that the library can be found in, and the second
        entry is the name of the library. If `None` is returned for the path, the library is included in the
        necessary search paths to load it without an explicit path.
    """

    try:
        return find_library("sodium")
    except LibraryNotFoundException as e:
        raise Exception(
            "No locally installed version of libsodium found. Make sure libsodium is installed and can be"
            " found by Python/your C compiler."
        ) from e


libxeddsa_dir, libxeddsa_library = find_libxeddsa()
libsodium_dir, libsodium_library = find_libsodium()

library_dirs = []
if libxeddsa_dir is not None:
    library_dirs.append(libxeddsa_dir)
if libsodium_dir is not None:
    library_dirs.append(libsodium_dir)

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
