cd ${TRAVIS_BUILD_DIR}

export DEBIAN_LIBNACL_VERSION=1.6.1
export DEBIAN_CFFI_VERSION=1.12.2

python -m pip install --upgrade pip setuptools wheel
python -m pip --version

if [ $DEBIAN_DEPS ]
then
    python -m pip install --upgrade libnacl==$DEBIAN_LIBNACL_VERSION
    python -m pip install --upgrade cffi==$DEBIAN_CFFI_VERSION
else
    python -m pip install --upgrade libnacl
    python -m pip install --upgrade cffi
fi

python -m pip install pytest pylint

if [ "$TRAVIS_PYTHON_VERSION" != "pypy3" ]
then
    python -m pip install --upgrade mypy
fi

python -m pip install .
