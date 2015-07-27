.PHONY: test install

setup:
	pip install --upgrade -r requirements.txt

install:
	python setup.py install

test:
	nosetests --rednose

test-coverage:
	nosetests --rednose --with-coverage --cover-xml --cover-package=sinor
