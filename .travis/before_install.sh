#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    echo "brew update"
    brew update
    echo "brew install pyenv"
    brew install pyenv
    echo "brew install pyenv-virtualenv"
    brew install pyenv-virtualenv
    echo "pyenv install $PYTHON_VERSION"
    pyenv install $PYTHON_VERSION
    echo "pyenv virtualenv $PYTHON_VERSION virtualenv"
    pyenv virtualenv $PYTHON_VERSION virtualenv
    echo "pyenv activate virtualenv"
    pyenv activate virtualenv
    echo "python --version"
    python --version
    echo "pip install --upgrade pip setuptools wheel"
    pip install --upgrade pip setuptools wheel
    echo "pip --version"
    pip --version
fi
