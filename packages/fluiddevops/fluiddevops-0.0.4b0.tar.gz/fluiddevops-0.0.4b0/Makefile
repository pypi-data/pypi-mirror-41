
help:
	@cat Makefile

develop:
	python setup.py develop

install:
	python setup.py install

clean_pyc:
	find fluiddevops -name "*.pyc" -delete
	find fluiddevops -name "__pycache__" -type d | xargs rm -rf

clean: clean_pyc
	rm -rf build dist

deploy: clean
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload dist/*

tests:
	HGRCPATH="${PWD}/.ci/hgrc" \
	python -m unittest discover -v

_tests_coverage:
	mkdir -p .coverage
	HGRCPATH="${PWD}/.ci/hgrc" \
	coverage run -m unittest discover

_report_coverage:
	coverage report
	coverage html
	coverage xml
	@echo "Code coverage analysis complete. View detailed report:"
	@echo "file://${PWD}/.coverage/index.html"

coverage: _tests_coverage _report_coverage

black:
	black -l 82 fluiddevops
	hg commit -m "Apply $(shell black --version)"
