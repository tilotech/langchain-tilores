all: setup test

check:
	@test -f .envrc || (echo "Please setup your .envrc, see .envrc.example" && exit 1)

setup: check
	pip install .[test,all]

test: check
	python -m unittest tests/*_test.py

