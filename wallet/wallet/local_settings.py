from .settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or
        # 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        # Or path to database file if using sqlite3.
        'NAME': 'codebits-wallet',
        'USER': 'root',                         # Not used with sqlite3.
        'PASSWORD': 'root',                    # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': 'localhost',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',
    }
}
