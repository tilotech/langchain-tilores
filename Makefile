.PHONY: build
all: setup test

check:
	@test -f .envrc || (echo "Please setup your .envrc, see .envrc.example" && exit 1)

setup: check
	pip install .[test,all]

test: check
	python -m unittest tests/*_test.py

build:
	python -m build

upload: build
	-twine upload --repository testpypi dist/*
	twine upload dist/*

