from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'read_default_file': 'settings/main.cnf',
    }
}