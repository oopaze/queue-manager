test:
	python -m pytest --verbose -s

setup:
	python3 -m pip install virtualenv
	python3 -m virtualenv .venv
	# python3 .venv/Scripts/activate_this.py # windows
	. .venv/bin/activate # linux
	python -m pip install -r requirements.txt

runserver:
	python runserver.py

tv:
	python example_tv.py

ts:
	python example_ts.py

ta:
	python example_ta.py

