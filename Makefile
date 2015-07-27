.PHONY: test install

setup:
	pip install --upgrade -r requirements.txt

install:
	python setup.py install

test:
	nosetests --rednose
