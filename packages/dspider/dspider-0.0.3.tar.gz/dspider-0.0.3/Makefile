ifneq ($(shell [ -f ./.venv/bin/python ] && echo 1),1)

all:

install-deps: $(shell find Pipfile -type f)
	python3 -m virtualenv .venv
	.venv/bin/python -m pip install -U pip pipenv
	.venv/bin/pipenv install --dev --deploy

install-deps-without-dev: $(shell find Pipfile -type f)
	python3 -m virtualenv .venv
	.venv/bin/python -m pip install -U pip pipenv
	.venv/bin/python install --deploy

%:
	@echo "virtualenv missing! Please execute:"
	@echo "make install-deps"

else

ifneq ($(shell ./.venv/bin/python -c "import sys;print(sys.executable)"),$(shell which python))

all:

%:
	@echo "virtualenv deactivated! Please execute:"
	@echo "source ./.venv/bin/acitvate"

else

all: test

isort: .isort

.isort: $(shell find dspider -type d) \
		$(shell find tests -type d)
	isort -rc dspider tests
	@touch .isort

flake: .flake

.flake: $(shell find dspider -type d) \
		$(shell find tests -type d)
	flake8 dspider tests
	@touch .flake

black: .black

.black: $(shell find dspider -type d) \
		$(shell find tests -type d)
	black dspider tests
	@touch .black

mypy: .mypy

.mypy: $(shell find dspider -type d)
	mypy dspider
	@touch .mypy

.develop: $(shell find dspider -type d) .isort .black .flake
	@touch .develop

test: .develop
	pytest -q -x --ff --nf

vtest: .develop
	pytest -vv -x --ff --nf

cov: .develop
	pytest -vv --cov=dspider
	coverage html
	@echo "open file://`pwd`/htmlcov/index.html to see coverage"

clean:
	@rm -f .black
	@rm -f .coverage
	@rm -f .develop
	@rm -f .flake
	@rm -f .isort
	@rm -f .mypy
	@rm -rf .pytest_cache
	@rm -rf htmlcov
	@rm -rf *.egg-info
	@rm -rf build
	@rm -rf dist

build:
	python setup.py sdist bdist_wheel


.PHONY: all isort flake black mypy test vtest cov clean build

endif
endif
