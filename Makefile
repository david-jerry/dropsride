VIRTUALENV = $(shell cd ; pwd)/.local/share/virtualenvs/darkcodr-OkfsPW01
PYTHON = $(VIRTUALENV)/bin/python
ISORT = isort $$(find $(PWD)/dropsride -not -path '*/migrations/*' -type f -name '*.py' -not -name '__init__.py' -print)


activate_venv:
	( cd .. ; pipenv shell ; cd dropsride )

deps:
	( $(PYTHON) -m pip install -r requirements/local.txt)

migrations:
	( $(PYTHON) ./manage.py makemigrations ; $(PYTHON) ./manage.py migrate )

countries_plus:
	( $(PYTHON) ./manage.py update_countries_plus )

management_commands:
	( $(PYTHON) ./manage.py get_currency_exchange ; $(PYTHON) ./manage.py get_ng_banks )

po:
	( $(PYTHON) ./manage.py makemessages -a -e html,txt,py )

mo:
	( $(PYTHON) ./manage.py compilemessages )

isort-fix:
	$(ISORT)

.PHONY:						\
	po						\
	mo						\
	isort-fix

.INSTALL:					\
	deps					\
	migrations				\
	po						\
	mo						\

.RUNDEV:					\
	migrations				\
	countries_plus			\
	po						\
	mo						\
	management_commands

