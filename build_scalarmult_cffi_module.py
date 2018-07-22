from __future__ import print_function

import cffi
import os

bin_directory     = os.path.abspath("ref10/bin")
library_directory = os.path.abspath("ref10/crypto_scalarmult")
library_header    = os.path.join(library_directory, "module.preprocessed")

ffibuilder = cffi.FFI()

# Load the header.
with open(library_header) as f:
    ffibuilder.cdef(f.read())

# Define how to compile the python module.
ffibuilder.set_source(
    "_crypto_scalarmult",
    '#include "' + library_header + '"',
    libraries    = [ "crypto_scalarmult" ],
    library_dirs = [ bin_directory ]
)

if __name__ == "__main__":
    # Compile the code into a python module.
    ffibuilder.compile()

    print("Make sure the shared objects can be found by Python:")
    print('export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:' + bin_directory + '"')
