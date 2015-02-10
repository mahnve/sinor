.PHONY: test install

install:
	python setup.py install

test:
	nosetests
