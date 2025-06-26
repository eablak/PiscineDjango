#!/bin/bash   

VENV_DIR="local_lib"
LOG_FILE="pip_install.log"
URL_PATH="https://github.com/jaraco/path.git"


pip --version

python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

pip install --log $LOG_FILE --force-reinstall git+$URL_PATH

python3 "my_program.py"