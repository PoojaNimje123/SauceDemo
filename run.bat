@echo off
call venv\scripts\activate
pytest -v -s --html=Report/FirefoxReport.html --browser Firefox
pause
