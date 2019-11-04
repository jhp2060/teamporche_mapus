from .base import *

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DEBUG = False

ALLOWED_HOSTS = secrets['ALLOWED_HOST']

DATABASES = {
    'default': secrets['DB_SETTINGS']['PRODUCTION']
}