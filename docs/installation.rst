Installation
============

python-xeddsa depends on two system libraries, `libxeddsa <https://github.com/Syndace/libxeddsa>`_ and `libsodium <https://download.libsodium.org/doc/>`_.

Install the latest release using pip (``pip install XEdDSA``) or manually from source by running ``pip install .`` (preferred) or ``python setup.py install`` in the cloned repository. The installation requires libsodium and the Python development headers to be installed. If a locally installed version of libxeddsa is available, python-xeddsa tries to use that. Otherwise it uses prebuilt binaries of the library, which are available for Linux, MacOS and Windows on the amd64 architecture. Set the ``LIBXEDDSA_FORCE_LOCAL`` environment variable to forbid the usage of prebuilt binaries.