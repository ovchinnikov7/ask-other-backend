#! /bin/bash

python3 manage.py migrate --noinput
python3 manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL
python3 manage.py runserver 0.0.0.0:8000
