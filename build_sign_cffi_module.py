from __future__ import print_function

import cffi
import os

MODULE_NAME = "crypto_sign"

library_header = os.path.abspath("ref10/" + MODULE_NAME + "/module.preprocessed")
static_lib_dir = os.path.abspath("ref10/bin/static/")

ffibuilder = cffi.FFI()

# Load the header.
with open(library_header) as f:
    ffibuilder.cdef(f.read())

# Define how to compile the python module.
ffibuilder.set_source(
    "_" + MODULE_NAME,
    '#include "' + library_header + '"',
    library_dirs = [ static_lib_dir ],
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
)

if __name__ == "__main__":
    # Compile the code into a python module.
    ffibuilder.compile()
