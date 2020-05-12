# practica-api

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/40de1c4030584dea97eefaf17cf75e3b)](https://app.codacy.com/app/sumanthratna/practica-api?utm_source=github.com&utm_medium=referral&utm_content=sumanthratna/practica-api&utm_campaign=Badge_Grade_Dashboard)

Your code should have the following structure:

    ├── run.sh
    ├── private
    │   ├── ...
    └── public
        ├── <THIS REPO>

`run.sh` should have the following contents (on [Director](https://director.tjhsst.edu/), `run.sh` starts at `public/`):

```bash
#!/bin/env/bash

export DEBUG=FALSE

rm -rf venv/
python3.6 -m venv venv
source venv/bin/activate
python3 -m pip install wheel gunicorn
python3 -m pip install -r requirements.txt

rm -rf static/
python manage.py collectstatic --no-input
gunicorn practica_api.wsgi -b 127.0.0.1:$PORT -w=1
deactivate
```

If Python 3.6+ is not available on your Ubuntu server and you do not have `sudo` access, add the following after `export DEBUG=FALSE` in `run.sh`:

```bash
# adapted from https://randomwalk.in/python/2019/10/27/Install-Python-copy.html
cd ..
wget https://www.python.org/ftp/python/3.6.10/Python-3.6.10.tgz
tar zxfv Python-3.6.10.tgz
rm Python-3.6.10.tgz
find ./Python-3.6.10/Python -type d | xargs chmod 0755
cd Python-3.6.10
./configure --prefix=$PWD/Python-3.6.10/Python
make
make install
ln -s python python3.6
cd ../public
export PATH=../Python-3.6.10:$PATH
```

Alternatively, you can download the appropriate [pypy](https://www.pypy.org/) [build](https://www.pypy.org/download.html#python-3-6-compatible-pypy3-6-v7-3-1) and `scp` it to your server. The production server uses pypy3. 
