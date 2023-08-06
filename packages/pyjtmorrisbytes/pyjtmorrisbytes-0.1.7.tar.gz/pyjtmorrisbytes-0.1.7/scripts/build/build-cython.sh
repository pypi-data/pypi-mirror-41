#!/usr/bin/bash

# ensure that the correct python version is installed
python --version

# insure that pip, setuptools and wheel are installed
curl -O https://bootstrap.pypa.io/get-pip.py
# run get-pip
python get-pip.py --user

pip install cython --user
echo "Compiling pyx to .c, html, and .so files files"
cd src
cythonize -a -i -f -3 $(find -name *.pyx)
cd ..
