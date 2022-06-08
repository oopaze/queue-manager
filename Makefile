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
	$(_python) devops/example_tv.py

ts:
	$(_python) devops/example_ts.py

ta:
	$(_python) devops/example_ta.py

docker_run:
	docker-compose up --build

docker_purge:
	bash ./docker-purge.sh

