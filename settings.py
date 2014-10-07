import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '7#brsp@h-ev(eyu68u5vh4rv*8d%c8mn^@wkgtp5l@56(8$u(='

INSTALLED_APPS = ('performance',)

MIDDLEWARE_CLASSES = ()

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_performance',
        'USER': 'postgres',
        'PASSWORD': 'waffle',
        'HOST': 'localhost',
        'PORT': '',
        'CONN_MAX_AGE': None
    }
}
