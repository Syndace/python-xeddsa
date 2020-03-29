cd ${TRAVIS_BUILD_DIR}

case "$TRAVIS_PYTHON_VERSION" in
"3.6")
    export OSX_PYTHON_VERSION="3.6.9"
    export WIN_PYTHON_VERSION="3.6.8"
    export WIN_PYTHON_DIR_NAME="Python36"
    ;;
"3.7")
    export OSX_PYTHON_VERSION="3.7.5"
    export WIN_PYTHON_VERSION="3.7.7"
    export WIN_PYTHON_DIR_NAME="Python37"
    ;;
"3.8")
    export OSX_PYTHON_VERSION="3.8.2"
    export WIN_PYTHON_VERSION="3.8.2"
    export WIN_PYTHON_DIR_NAME="Python38"
    ;;
"pypy3")
    export OSX_PYTHON_VERSION="pypy3.6-7.3.0"
    # On Windows, pypy3 is only available in a 32 bit build.
    # 32 bit is not supported by this package (officially).
    ;;
*)
    echo "Ugh! Looks like someone forgot to update their build files correctly!"
    ;;
esac

if [ "$TRAVIS_OS_NAME" = "linux" ]
then
    true # Nothing special to do on Linux
fi

if [ "$TRAVIS_OS_NAME" = "osx" ]
then
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    pyenv install $OSX_PYTHON_VERSION
    pyenv virtualenv $OSX_PYTHON_VERSION virtualenv
    pyenv activate virtualenv
fi

if [ "$TRAVIS_OS_NAME" = "windows" ]
then
    export PATH="/c/$WIN_PYTHON_DIR_NAME:/c/$WIN_PYTHON_DIR_NAME/Scripts:$PATH"
    choco install python --version $WIN_PYTHON_VERSION

    # Download and install libsodium
    wget https://download.libsodium.org/libsodium/releases/libsodium-1.0.18-stable-msvc.zip
    unzip libsodium-1.0.18-stable-msvc.zip
    mv libsodium/x64/Release/v141/static/libsodium.lib libxeddsa/
    mv libsodium/x64/Release/v141/dynamic/libsodium.dll /c/Windows/System32/
fi
