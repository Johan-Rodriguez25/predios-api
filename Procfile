release: Python manage.py makemigrations --no-input
release : Python manage.py migrate --no-input

web: gunicorn prediosAPIProject.wsgi --log-file=-