"""
config.py will be storing all the module configs.
"""

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'a secret key is afoot you best be movin along'

SQLALCHEMY_DATABASE_URI = f'sqlite:///{_basedir}/data-dev.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CSRF_ENABLED = True
CSRF_SESSION_KEY = ""

BRAND = "reddit"
ROOT_URL = "http://localhost:20000"
