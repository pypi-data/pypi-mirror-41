#!/bin/bash

#
# Source the virtual environment (assumed to be in _venv) and then
# run pytest on the specified directory/file with a coverage report 
#

if [ ! -e _venv ]
then
    echo "Cannot find virtualenvironment directory _venv"
    exit 1
fi

source _venv/bin/activate
pytest --cov=libgs "$@"
