# practica-api
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/40de1c4030584dea97eefaf17cf75e3b)](https://app.codacy.com/app/sumanthratna/practica-api?utm_source=github.com&utm_medium=referral&utm_content=sumanthratna/practica-api&utm_campaign=Badge_Grade_Dashboard)

`run.sh`:
```bash
#!/bin/bash

export DEBUG=FALSE

rm -rf venv/
python3 -m venv venv
source venv/bin/activate
python3 -m pip install wheel gunicorn
python3 -m pip install -r requirements.txt

rm -rf static/
python manage.py collectstatic --no-input
gunicorn practica_api.wsgi -b 127.0.0.1:$PORT -w=1
deactivate
```