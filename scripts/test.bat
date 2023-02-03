python -m venv .venv
CALL .\.venv\Scripts\activate.bat
pip install -r .\requirements.txt
python -m pytest .\tests
SET /A tests_exit_code=%ERRORLEVEL%
deactivate
EXIT /B %tests_exit_code%
