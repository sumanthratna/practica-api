#!/bin/bash

cd practica-api
export DEBUG=FALSE
source venv/bin/activate
gunicorn practica_api.wsgi -b 127.0.0.1:$PORT -w=4