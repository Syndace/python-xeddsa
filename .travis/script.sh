cd ${TRAVIS_BUILD_DIR}

export MYPYPATH=stubs/

if [ "$TRAVIS_PYTHON_VERSION" != "pypy3" ]
then
    python -m mypy xeddsa/
fi

python -m pylint xeddsa/
python -m pytest
