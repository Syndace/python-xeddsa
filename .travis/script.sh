cd ${TRAVIS_BUILD_DIR}

export MYPYPATH=stubs/

if [ "$TRAVIS_PYTHON_VERSION" != "pypy3" ]
then
    python -m mypy --strict xeddsa/
    python -m mypy --strict tests/
    python -m mypy --strict libxeddsa/
fi

python -m pylint xeddsa/
python -m pylint tests/*.py
python -m pylint libxeddsa/*.py
python -m pytest
