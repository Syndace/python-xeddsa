from __future__ import absolute_import
from __future__ import print_function

import cffi
import os
import subprocess
import sys
import zipfile

try:
    # Python 3
    from urllib.request import urlopen
except:
    # Python 2
    from urllib2 import urlopen

ref10_dir  = os.path.abspath("ref10")
module_dir = os.path.join(ref10_dir, "crypto_sign")
bin_dir    = os.path.join(ref10_dir, "bin")
build_dir  = os.path.join(ref10_dir, "build")

library_header = os.path.join(module_dir, "module.h")

try:
    os.mkdir(build_dir)
except OSError:
    pass

libraries = [
    "crypto_sign_static",
    "crypto_hash_static",
    "crypto_hashblocks_static",
    "crypto_verify_static",
    "fastrandombytes_static",
    "kernelrandombytes_static",
    "crypto_rng_static",
    "crypto_stream_static",
    "crypto_core_static"
]

class UnknownSystemException(Exception):
    pass

if os.name == "posix":
    # On UNIX, we HAVE to make the ref10 libraries, because the kernelrandombytes module
    # can vary between different UNIX systems.
    print("Attempting to compile the ref10 library...")
    print("The compilation requires CMake and the \"make\" tool.")
    print("The \"cmake\" and \"make\" commands are used.")

    subprocess.check_call([ "cmake", "-G", "Unix Makefiles", ".." ], cwd = build_dir)
    subprocess.check_call([ "make" ], cwd = build_dir)

    print("Library built successfully!")
elif os.name == "nt":
    libraries += [ "ADVAPI32" ]

    # On Windows, there is only one possible version of the kernelrandombytes module:
    # rtlgenrandom. Thus, precompiled binaries can be used.
    print("Attempting to compile the ref10 library...")
    print("The compilation requires CMake and a MinGW environment.")
    print("The \"cmake\" and \"mingw32-make\" commands are used.")

    try:
        subprocess.check_call([ "cmake", "-G", "MinGW Makefiles", ".." ], cwd = build_dir)
        subprocess.check_call([ "mingw32-make" ], cwd = build_dir)

        print("Library built successfully!")
    except subprocess.CalledProcessError:
        print("Compiling the ref10 library failed.")
        print("Attempting to download precompiled binaries...")

        # The recommended way to detect 64-bit and 32-bit systems according to
        # https://docs.python.org/3/library/platform.html#cross-platform
        is_32bit = sys.maxsize == 2 ** 31 - 1
        is_64bit = sys.maxsize == 2 ** 63 - 1

        if not is_32bit and not is_64bit:
            raise UnknownSystemException(
                "This system was detected as neither 32-bit nor 64-bit."
            )

        precompiled_windows_32bit = (
            "https://github.com/Syndace/python-xeddsa/releases/download/v0.4.3-beta/" +
            "bin-windows-x86.zip"
        )

        precompiled_windows_64bit = (
            "https://github.com/Syndace/python-xeddsa/releases/download/v0.4.3-beta/" +
            "bin-windows-amd64.zip"
        )

        url = precompiled_windows_64bit if is_64bit else precompiled_windows_32bit

        zip_location = os.path.join(ref10_dir, "bin.zip")

        print("Downloading precompiled binaries...")
        print("Make sure the system can access https://github.com.")

        zip_memory = urlopen(url)
        with open(zip_location, "wb") as zip_file:
            zip_file.write(zip_memory.read())
        zip_memory.close()

        binaries_zipfile = zipfile.ZipFile(zip_location)
        binaries_zipfile.extractall(ref10_dir)
        binaries_zipfile.close()

        os.remove(zip_location)

        print("Precompiled binaries downloaded!")
else:
    raise UnknownSystemException(
        "Unsupported operating system (neither UNIX nor Windows)."
    )

ffibuilder = cffi.FFI()

# Load the header.
with open(library_header) as f:
    ffibuilder.cdef(f.read())

# Define how to compile the python module.
ffibuilder.set_source(
    "_crypto_sign",
    '#include "' + library_header + '"',
    library_dirs = [ bin_dir ],
    libraries    = libraries
)

if __name__ == "__main__":
    # Compile the code into a python module.
    ffibuilder.compile()
