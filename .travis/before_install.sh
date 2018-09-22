#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew install pyenv-virtualenv
    pyenv virtualenv $PYTHON_VERSION virtualenv
    pyenv activate virtualenv
    python --version
    pip install --upgrade pip setuptools wheel
    pip --version
fi
