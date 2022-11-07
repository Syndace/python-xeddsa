import os
import platform

import cffi  # type: ignore[import]

ffibuilder = cffi.FFI()

libxeddsa_header = os.path.join(os.path.dirname(os.path.abspath(__file__)), "xeddsa.h")

with open(libxeddsa_header, encoding="utf-8") as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    "_libxeddsa",
    '#include "' + libxeddsa_header + '"',
    libraries=[ "libxeddsa", "libsodium" ] if platform.system() == "Windows" else [ "xeddsa", "sodium" ]
)

if __name__ == "__main__":
    ffibuilder.compile()
