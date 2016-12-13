
#FlaskTasr/config.py

import os

#grab the folder where this script livees
basedir = os.path.abspath(os.path.dirname(__file__))


DATABASE = 'flasktaskr.db'
#USERNAME = 'admin'
#PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'montevideo'

#define the full path for the databasae
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DATABASE_PATH



