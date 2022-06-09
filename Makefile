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
	$(_python) runclient_tv.py

ts:
	$(_python) runclient_ts.py

ta:
	$(_python) runclient_ta.py

docker_run_server:
	docker-compose -f docker-compose.server.yml up --build

docker_run:
	docker-compose up --build

docker_purge:
	bash ./docker-purge.sh

