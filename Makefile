MANAGE_PY = python django/manage.py
SETTINGS_DEV = --settings=luizalabs_school.settings.development

check:clean
	$(MANAGE_PY) check $(SETTINGS_DEV)

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf

dbshell:
	$(MANAGE_PY) dbshell $(SETTINGS_DEV)

migrate:
	$(MANAGE_PY) migrate $(SETTINGS_DEV)

migrations:
	$(MANAGE_PY) makemigrations $(SETTINGS_DEV)

run:
	$(MANAGE_PY) runserver $(SETTINGS_DEV)

shell:
	$(MANAGE_PY) shell $(SETTINGS_DEV)

test:
	pytest -x django/luizalabs_school
