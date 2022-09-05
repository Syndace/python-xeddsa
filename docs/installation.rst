Installation
============

python-xeddsa depends on two system libraries, `libxeddsa <https://github.com/Syndace/libxeddsa>`__>=2,<3, and `libsodium <https://download.libsodium.org/doc/>`__.

Install the latest release using pip (``pip install XEdDSA``) or manually from source by running ``pip install .`` (preferred) or ``python setup.py install`` in the cloned repository. The installation requires libsodium and the Python development headers to be installed. If a locally installed version of libxeddsa is available, python-xeddsa tries to use that. Otherwise it uses prebuilt binaries of the library, which are available for Linux, MacOS and Windows on the amd64 architecture, and potentially for MacOS arm64 too. Set the ``LIBXEDDSA_FORCE_LOCAL`` environment variable to forbid the usage of prebuilt binaries.

Usage with Brython
------------------

python-xeddsa can be used in the browser with Brython, thanks to the Emscripten build of libxeddsa. Refer to ``tests/test_brython.html`` for the setup routine required to load the Emscripten build for usage with Brython. In summary, Brython's initialization is deferred until after the libxeddsa WebAssembly module and wrapper have been loaded. Other than that, python-xeddsa can be used as usual and handled with Brython like a pure Python package.
