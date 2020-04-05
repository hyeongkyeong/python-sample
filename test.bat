set PYTHONPATH=%PYTHONPATH%;%cd%
coverage run --rcfile=.coveragerc test.py
coverage report -m
coverage html 
coverage xml
coverage json --pretty-print