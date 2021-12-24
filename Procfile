release: python manage.py makemigrations
release : python manage.py migrate

web: gunicorn prediosAPIProject.wsgi --log-file=-