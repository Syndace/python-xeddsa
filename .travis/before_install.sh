#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    echo "> brew update"
    brew update
    echo "> brew install pyenv"
    brew install pyenv
    echo "> brew install pyenv-virtualenv"
    brew install pyenv-virtualenv
    echo "> brew upgrade pyenv"
    brew upgrade pyenv
    echo "> brew upgrade pyenv-virtualenv"
    brew upgrade pyenv-virtualenv
    echo "> eval \"$(pyenv init -)\""
    eval "$(pyenv init -)"
    echo "> eval \"$(pyenv virtualenv-init -)\""
    eval "$(pyenv virtualenv-init -)"
    echo "> pyenv install $PYTHON_VERSION"
    pyenv install $PYTHON_VERSION
    echo "> pyenv virtualenv $PYTHON_VERSION virtualenv"
    pyenv virtualenv $PYTHON_VERSION virtualenv
    echo "> pyenv activate virtualenv"
    pyenv activate virtualenv
    echo "> python --version"
    python --version
    echo "> pip install --upgrade pip setuptools wheel"
    pip install --upgrade pip setuptools wheel
    echo "> pip --version"
    pip --version

    echo "> brew install libsodium"
    brew install libsodium
else
    sudo apt update
    sudo apt install libsodium18
fi
