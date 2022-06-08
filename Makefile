_python = . venv/bin/activate; python

test:
	$(_python) -m pytest --verbose -s

setup: requirements.txt
	python3 -m pip install virtualenv
	python3 -m virtualenv venv
	$(_python) -m pip install -r requirements.txt

runserver:
	$(_python) runserver.py

tv:
	$(_python) example_tv.py

ts:
	$(_python) example_ts.py

ta:
	$(_python) example_ta.py

