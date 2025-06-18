VENV_DIR="django_venv"
LOG_FILE="pip_install.log"


python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

python3 -m pip install --log $LOG_FILE --force-reinstall -r requirement.txt