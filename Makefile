runserver-local: migrate
	python manage.py runserver --settings=settings.local

newmigrations:
	python manage.py makemigrations --settings=settings.local

migrate:
	python manage.py migrate --settings=settings.local

environment:
	c:\Users\tod24\Desktop\Python\Django_F\env\Scripts\Activate.ps1