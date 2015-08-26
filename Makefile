#!/usr/bin/make
# WARN: gmake syntax
########################################################
# Makefile for Sudoku
#
# useful targets:
#   make dev ------------------ install development requirements
#   make tests ---------------- run the tests
#   make pyflakes, make pep8 -- source code checks

ENV=$(CURDIR)/env

dev:
	virtualenv $(ENV) --system-site-packages --clear
	$(ENV)/bin/pip install -e .
	$(ENV)/bin/pip install -r test-requirements.txt
	$(ENV)/bin/pip install --upgrade pyformat isort

tests:
	$(ENV)/bin/py.test src

format:
	find src/sudoku/ -type f -name '*.py' -exec isort --settings-path $(CURDIR) {} \;
	pyformat -r -i --exclude _version.py src/ setup.py

loc:
	sloccount src

pep8:
	@echo "#############################################"
	@echo "# Running PEP8 Compliance Tests"
	@echo "#############################################"
	-pep8 -r --ignore=E501,E221,W291,W391,E302,E251,E203,W293,E231,E303,E201,E225,E261,E241 --exclude _version.py src/

pyflakes:
	pyflakes src/sudoku/*.py src/sudoku/*/*.py


lynt: format pep8 pyflakes loc


.PHONY: dev tests loc pep8 pyflakes format style
