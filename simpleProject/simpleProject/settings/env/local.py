# Project modules
from settings.base import *


DEBUG = True
ALLOWED_HOSTS = []
DJANGORLAR_ENV_ID = 'local'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    },
}