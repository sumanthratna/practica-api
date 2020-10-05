# practica-api

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/40de1c4030584dea97eefaf17cf75e3b)](https://app.codacy.com/app/sumanthratna/practica-api?utm_source=github.com&utm_medium=referral&utm_content=sumanthratna/practica-api&utm_campaign=Badge_Grade_Dashboard) [![Build Status](https://travis-ci.com/sumanthratna/practica-api.svg?branch=master)](https://travis-ci.com/sumanthratna/practica-api)

Your code should have the following structure:

    ├── run.sh
    ├── private
    │   ├── ...
    └── public
        ├── <THIS REPO>

`run.sh` should have the following contents (on [Director](https://director.tjhsst.edu/), `run.sh` starts at `public/`):

```sh
#!/bin/sh

# This assumes you've created a virtual environment and installed Gunicorn

source venv/bin/activate

python manage.py collectstatic --no-input
gunicorn --bind $HOST:$PORT --workers 1 'practica_api.wsgi:application'
```
