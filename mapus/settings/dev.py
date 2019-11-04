import os
from .base import *

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mapus',
        'USER': 'root',
        'PASSWORD': '1234',
        'PORT': 5432,
    }
}
