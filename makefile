lint:
	flake8
#	mypy app.py

test:
	python -m unittest discover

package:
	docker build . -t python-flask:latest

deploy:
	docker-compose up

undeploy:
	docker-compose down

all: lint test package deploy