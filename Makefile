runserver-local: migrate
	python manage.py runserver --settings=settings.local

newmigrations:
	python manage.py makemigrations --settings=settings.local

migrate:
	python manage.py migrate --settings=settings.local

environment:
	.\env\Scripts\Activate.ps1

createsuperuser:
	python manage.py createsuperuser --settings=settings.local

tests:
	python manage.py test --settings=settings.local

test-one:
	python manage.py test $(TEST_NAME) --settings=settings.local

shellplus:
	python manage.py shell-plus --ipython --settings=settings.local