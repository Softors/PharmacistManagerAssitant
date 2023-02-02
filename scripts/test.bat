python -m venv .venv
CALL .\.venv\Scripts\activate.bat
pip install -r .\requirements.txt
python -m pytest .\tests
deactivate
