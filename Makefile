init:
	pip install -r requirements.txt

test:
	python tests/*.py

install:
	make init
	python ./setup.py install
