cd ${TRAVIS_BUILD_DIR}

export MYPYPATH=stubs/

if [ "$TRAVIS_PYTHON_VERSION" != "pypy3" ]
then
    python -m mypy --strict xeddsa/ setup.py libxeddsa/ tests/
fi

python -m pylint xeddsa/ setup.py libxeddsa/ tests/
python -m flake8 xeddsa/ setup.py libxeddsa/ tests/
python -m pytest
