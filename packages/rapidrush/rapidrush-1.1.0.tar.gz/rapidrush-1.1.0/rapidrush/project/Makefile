SOURCEHEADER

.PHONY: test install test_require clean version version_short push pypi

BLACK = black PACKAGENAME; black tests

test:
	@coverage erase
	@coverage run --source=PACKAGENAME -m unittest discover -v
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
	@rm -rf PACKAGENAME.egg-info
	@rm -rf .tox
	@rm -rf symbolink
	@rm .coverage

version:
	@python3 -c "import tests"

version_short:
	@python3 -c "import PACKAGENAME; print(PACKAGENAME.__version__)"

black:
	$(BLACK)

push: black test clean
	git push origin HEAD

pypi: black test clean
	python3 setup.py sdist bdist_wheel && twine upload dist/*

pypitest: black test clean
	python3 setup.py sdist bdist_wheel && twine upload --repository-url https://test.pypi.org/legacy/ dist/*
