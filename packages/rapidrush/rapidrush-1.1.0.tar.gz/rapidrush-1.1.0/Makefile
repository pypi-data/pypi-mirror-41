# Copyright (c) 2019 bluelief.
# This source code is licensed under the MIT license.

.PHONY: test install test_require clean version version_short push pypi

BLACK = black rapidrush; black tests

test:
	@coverage erase
	@coverage run --source=rapidrush -m unittest discover -v
	@coverage report --show-missing

install:
	python3 setup.py install

test_require:
	pip3 install -r test-requirements.txt

clean:
	@find ./ -name "__pycache__" -exec rm -rf "{}" +;
	@find ./ -name "*.pyc" -exec rm -rf "{}" +;
	@rm -rf build
	@rm -rf dist
	@rm -rf rapidrush.egg-info
	@rm -rf .tox
	@rm -rf symbolink
	@rm -rf .coverage

version:
	@python3 -c "import tests"

version_short:
	@python3 -c "import rapidrush; print(rapidrush.__version__)"

black:
	$(BLACK)

push: black test clean
	git push origin HEAD

pypi: black test clean
	python3 setup.py sdist bdist_wheel && twine upload dist/*

pypitest: black test clean
	python3 setup.py sdist bdist_wheel && twine upload --repository-url https://test.pypi.org/legacy/ dist/*
