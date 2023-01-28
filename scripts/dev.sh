#!/bin/sh
python -m venv .venv
. .venv/bin/activate
pip install -r ./requirements.txt
python -m pma
deactivate
