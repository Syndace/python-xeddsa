cd ${TRAVIS_BUILD_DIR}

export DEBIAN_CFFI_VERSION=1.14.5

python -m pip install --upgrade pip setuptools wheel
python -m pip --version
python -m pip install pytest pylint flake8

if [ "$TRAVIS_PYTHON_VERSION" != "pypy3" ]
then
    python -m pip install --upgrade mypy
fi

if [ $DEBIAN_DEPS ]
then
    python -m pip install --upgrade cffi==$DEBIAN_CFFI_VERSION
else
    python -m pip install --upgrade cffi
fi

python -m pip install .
