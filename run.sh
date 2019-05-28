#!/bin/bash

rm -rf static/
cd practica-api
export DEBUG=FALSE
source venv/bin/activate
rm -rf static/
python manage.py collectstatic --no-input
gunicorn practica_api.wsgi -b 127.0.0.1:$PORT -w=4