from __future__ import print_function

import cffi
import os
import platform
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

library_header = os.path.join(module_dir, "module.h")
static_lib_dir = os.path.join(bin_dir, "static")

libraries = [
    "crypto_sign",
    "crypto_hash",
    "crypto_hashblocks",
    "crypto_verify",
    "fastrandombytes",
    "kernelrandombytes",
    "crypto_rng",
    "crypto_stream",
    "crypto_core"
]

class UnknownSystemException(Exception):
    pass

if platform.system() == "Linux":
    # On Linux, we HAVE to make the ref10 libraries, because the kernelrandombytes module
    # can vary between different Linux systems.
    print("Compiling the ref10 library...")
    print("Make sure \"make\" and \"gcc\" are installed and available.")

    with open(os.devnull, "w") as psst:
        subprocess.check_call([ "make" ], cwd = ref10_dir, stdout = psst, stderr = psst)

    print("Library built successfully!")

elif platform.system() == "Windows":
    libraries = [ "lib" + library for library in libraries ] + [ "ADVAPI32" ]

    # On Windows, the kernelrandombytes module is fixed, thus we can use precompiled binaries.

    # The recommended way to detect 64-bit and 32-bit systems according to
    # https://docs.python.org/3/library/platform.html#cross-platform
    is_32bit = sys.maxsize == 2 ** 31 - 1
    is_64bit = sys.maxsize == 2 ** 63 - 1

    if not is_32bit and not is_64bit:
        raise UnknownSystemException("This system was detected as neither 32-bit nor 64-bit.")

    precompiled_windows_32bit = "https://github.com/Syndace/python-xeddsa/releases/download/v0.3.0-alpha/bin-windows-x86.zip"
    precompiled_windows_64bit = "https://github.com/Syndace/python-xeddsa/releases/download/v0.3.0-alpha/bin-windows-amd64.zip"

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

    print("Binaries downloaded!")

else:
    raise UnknownSystemException("This system was detected as neither Linux nor Windows.")

ffibuilder = cffi.FFI()

# Load the header.
with open(library_header) as f:
    ffibuilder.cdef(f.read())

# Define how to compile the python module.
ffibuilder.set_source(
    "_crypto_sign",
    '#include "' + library_header + '"',
    library_dirs = [ static_lib_dir ],
    libraries    = libraries
)

if __name__ == "__main__":
    # Compile the code into a python module.
    ffibuilder.compile()
