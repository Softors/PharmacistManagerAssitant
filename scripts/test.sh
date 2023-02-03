#!/bin/sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python -m pytest tests
TESTS_EXIT_CODE=$?
deactivate
exit $TESTS_EXIT_CODE
