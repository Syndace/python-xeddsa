from __future__ import print_function

import cffi
import os
import platform

class UnknownSystemException(Exception):
    pass

def buildLibraries(libraries):
    if platform.system() == "Windows":
        return [ "lib" + library for library in libraries ] + [ "ADVAPI32" ]
    if platform.system() == "Linux":
        return libraries
    raise UnknownSystemException()

MODULE_NAME = "crypto_sign"

ref10_dir  = os.path.abspath("ref10")
module_dir = os.path.join(ref10_dir, MODULE_NAME)
bin_dir    = os.path.join(ref10_dir, "bin")

library_header = os.path.join(module_dir, "module.h")
static_lib_dir = os.path.join(bin_dir, "static")

ffibuilder = cffi.FFI()

# Load the header.
with open(library_header) as f:
    ffibuilder.cdef(f.read())

# Define how to compile the python module.
ffibuilder.set_source(
    "_" + MODULE_NAME,
    '#include "' + library_header + '"',
    library_dirs = [ static_lib_dir ],
    libraries = buildLibraries([
        "crypto_sign",
        "crypto_hash",
        "crypto_hashblocks",
        "crypto_verify",
        "fastrandombytes",
        "kernelrandombytes",
        "crypto_rng",
        "crypto_stream",
        "crypto_core"
    ])
)

if __name__ == "__main__":
    # Compile the code into a python module.
    ffibuilder.compile()
