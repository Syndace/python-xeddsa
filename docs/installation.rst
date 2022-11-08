Installation
============

python-xeddsa depends on two system libraries, `libxeddsa <https://github.com/Syndace/libxeddsa>`__>=2,<3, and `libsodium <https://download.libsodium.org/doc/>`__.

Install the latest release using pip (``pip install XEdDSA``), from the wheels available in the artifacts of the `Test & Publish workflow <https://github.com/Syndace/python-xeddsa/actions/workflows/test-and-publish.yml>`_, or manually from source by running ``pip install .`` in the cloned repository. The installation from source requires libxeddsa, libsodium and the Python development headers to be installed.

Usage with Brython
------------------

python-xeddsa can be used in the browser with Brython, thanks to the Emscripten build of libxeddsa. Refer to ``tests/test_brython.html`` for the setup routine required to load the Emscripten build for usage with Brython. In summary, Brython's initialization is deferred until after the libxeddsa WebAssembly module and wrapper have been loaded. Other than that, python-xeddsa can be used as usual and handled with Brython like a pure Python package.
