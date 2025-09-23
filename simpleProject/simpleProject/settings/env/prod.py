# Project modules
from settings.base import *


DEBUG = False
ALLOWED_HOSTS = ["*"]
DJANGORLAR_ENV_ID = 'prod'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    },
}