#!/bin/bash
# This script should be ran inside the project root directory.
# Else the virtual environment will not be created in the proper location relative to "main.py".

echo "Please wait... Creating virtual environment for Python."
python3 -m venv .venv/ # Initialise virtual environment (python)
source .venv/bin/activate # Activate the virtual environment (python)
pip install --upgrade pip # Upgrade pip
pip install -r requirements.txt # Install from "requirements.txt"
deactivate # Deactivate the virtual environment (python), just to be sure.
echo "Script has finished!"
echo ""
echo "Before running the application, please activate the VENV!"
echo "* users on Linux can run: \"source .venv/bin/activate\""
echo "* users on Windows can run: \".venv\\Scripts\\activate\""
