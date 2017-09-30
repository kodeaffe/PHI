# PHI

This is a test Django project


# Installation (development)

It is assumed that the git checkout resides inside a project directory, e.g.  inside `/var/www/project` and thus to be found at `/var/www/project/PHI`. Files produced during installation or at runtime should be outside the git checkout to protect them from being overwritten. The notable exception is your local settings which have to be inside the Django project app's directory for Python to find them in its path. The directory tree might look like:

```
/var/www/project/
├── PHI
│   ├── phi
│   ├── import
│   ├── LICENSE
│   ├── README.md
│   ├── requirements.txt
└── venv
```

Paths in the commands below are relative to this README

## Install system packages

This depends on your OS, but on a Debian-based system, it looks like:

```bash
$ sudo apt install python3 postgresql virtualenv
```

If you have package issues when following the instructions below, you might have to install development packages like `python3-dev`.



## Configure PostgreSQL database

```bash
$ sudo -iu postgres
postgres@host:~$ psql
postgres=# CREATE DATABASE phi;
postgres=# CREATE USER phi WITH PASSWORD 'phi';
postgres=#> GRANT ALL PRIVILEGES ON DATABASE phi TO phi;
postgres=# \q
# exit
```


## Install virtualenv

```bash
$ virtualenv --python=python3 ../venv
$ source ../venv/bin/activate
(venv)$ pip install -r requirements.txt
```


## Configure Django settings

Edit `./phi/phi/local_settings.py` and configure database as above:

```python
# Used internally by Django, can be anything of your choice
SECRET_KEY = '<random string>'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'phi',
        'USER': 'phi',
        'PASSWORD': 'phi',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```


## Initialise database and create superuser

```bash
(venv)$ ./phi/manage.py migrate
(venv)$ ./phi/manage.py createsuperuser
```


## Run the project

```bash
(venv)$ ./phi/manage.py runserver
```

The application should be available at `http://localhost:8000`
Login to the Django admin is found at `http://localhost:8000/admin`


## Import construction systems

Existing construction systems can be imported using a CSV file. See
`import/head.csv` for an example header.

```bash
(venv)$ ./phi/manage.py import_construction_systems [filename]
```
