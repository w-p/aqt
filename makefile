.DEFAULT_GOAL := build

clean:
	@rm ./dist -fR
	@rm ./build -fR
	@rm ./aqt.egg-info -fR
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@pip uninstall -y aqt

build:
	python setup.py bdist_wheel

install:
	pip install $(shell find ./dist/ -type f -name *.whl)
