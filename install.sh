#!/bin/bash

# install dependencies
pip install python-dotenv
pip install --upgrade pip

# install Python >= 3.1
# create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
