set PYTHONPATH=%PYTHONPATH%;%cd%;%cd%\src
coverage run --rcfile=.coveragerc --append function_test.py
coverage report -m
coverage html 
coverage xml
coverage json --pretty-print