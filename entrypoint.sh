#!/bin/sh

python manage.py collectstatic --noinput

#python manage.py makemigrations
python manage.py migrate

# APP_PORT variable must be present in env
#Local mit runserver
#python manage.py runserver 0.0.0.0:${APP_PORT}
#Serverseitig mit Gunicorn
gunicorn btw_app.wsgi:application --bind 0.0.0.0:${APP_PORT}
