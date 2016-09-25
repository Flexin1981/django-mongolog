"""
Django settings for mongolog project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set to True to turn on verbose=True flag in test handlers
TEST_VERBOSITY = False
# Set the output level of the console logger.  'DEBUG' good for testing
CONSOLE = 'DEBUG'
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': CONSOLE,
            'class': 'settings.colorlog.ColorLogHandler',
            'info': 'white',
            'stream': 'ext://sys.stdout',
        },
        'simple': {
            'level': 'DEBUG',
            # Uncomment section to play with SimpleMongoLogHandler
            'class': 'mongolog.SimpleMongoLogHandler',
            'connection': 'mongodb://localhost:27017',
        },
        'http': {
            'level': 'DEBUG',
            # This section for HttpLogHandler
            'class': 'mongolog.HttpLogHandler',
            # Interesting Note:  requests 2.8.1 will turn this into a GET if it's missing a trailing slash
            # We automagically add the trailing slash
            'client_auth': 'http://192.168.33.51/4e487f07a84011e5a3403c15c2bcc424',
            'verbose': True,            
        },
        ################## Test Handlers
        'test_reference': {
            'level': 'DEBUG',
            'class': 'mongolog.SimpleMongoLogHandler',
            'connection': 'mongodb://localhost:27017',
            'w': 1,
            'j': False,

            # utc/local.  Only used with record_type=simple
            'time_zone': 'local',
            'verbose': TEST_VERBOSITY,
            'record_type': 'reference',
        },
        'test_embedded': {
            'level': 'DEBUG',
            'class': 'mongolog.SimpleMongoLogHandler',
            'connection': 'mongodb://localhost:27017',
            'w': 1,
            'j': False,

            # utc/local.  Only used with record_type=simple
            'time_zone': 'local',
            'verbose': TEST_VERBOSITY,
            'record_type': 'embedded',
        },
        'test_base_reference': {
            'level': 'DEBUG',
            'class': 'mongolog.BaseMongoLogHandler',
            'connection': 'mongodb://localhost:27017',
            'w': 1,
            'j': False,

            # utc/local.  Only used with record_type=simple
            'time_zone': 'local',
            'verbose': TEST_VERBOSITY,
            'record_type': 'reference',
        },
        'test_base_reference_w0': {
            'level': 'DEBUG',
            'class': 'mongolog.BaseMongoLogHandler',
            'connection': 'mongodb://localhost:27017',
            'w': 0,
            'j': False,

            # utc/local.  Only used with record_type=simple
            'time_zone': 'local',
            'verbose': TEST_VERBOSITY,
            'record_type': 'reference',
        },
        'test_base_invalid': {
            'level': 'DEBUG',
            'class': 'mongolog.BaseMongoLogHandler',
            'connection': 'mongodb://localhost:27017',
            'w': 0,
            'j': False,

            # utc/local.  Only used with record_type=simple
            'time_zone': 'local',
            'verbose': TEST_VERBOSITY,
            'record_type': 'reference',
        },
        'test_verbose': {
            'level': 'DEBUG',
            'class': 'mongolog.VerboseMongoLogHandler',
            'connection': 'mongodb://localhost:27017',
            'w': 0,
            'j': False,

            # utc/local.  Only used with record_type=simple
            'time_zone': 'local',
            'verbose': TEST_VERBOSITY,
            'record_type': 'reference',
        },
        'test_console': {
            'level': 'DEBUG',
            'class': 'settings.colorlog.ColorLogHandler',
            'info': 'white',
            'stream': 'ext://sys.stdout',
        },
        'test_http_invalid': {
            'level': 'DEBUG',
            # This section for HttpLogHandler
            'class': 'mongolog.HttpLogHandler',
            # Interesting Note:  requests 2.8.1 will turn this into a GET if it's missing a trailing slash
            # We automagically add the trailing slash
            'client_auth': 'http://192.168.33.51/4e487f07a84011e5a3403c15c2bcc424',
            'verbose': TEST_VERBOSITY,
            'timeout': 1,
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True
        },
        'console': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        },
        'simple': {
            'level': 'DEBUG',
            'handlers': ['simple'],
            'propagate': True
        },
        'http': {
            'level': 'DEBUG',
            'handlers': ['http'],
           'propagate': True,
        },
        ##################### Test Loggers
        'test': {
            'level': 'DEBUG',
            'propagate': False,
        },
        'test.reference': {
            'handlers': ['test_reference'],
        },
        'test.embedded': {
            'handlers': ['test_embedded'],
        },
        'test.base.reference': {
            'handlers': ['test_base_reference'],  
        },
        'test.base.reference.w0': {
            'handlers': ['test_base_reference_w0'],  
        },
        'test.base.invalid': {
            'handlers': ['test_base_invalid'],  
        },
        'test.verbose': {
            'handlers': ['test_verbose'],  
        },
        'test.http': {
            'level': 'DEBUG',
            'handlers': ['test_http_invalid'],
            'propagate': True,
        }
    },
}

SHELL_PLUS_PRE_IMPORTS = (
    'logging',
    ('logging', 'getLogger'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5^n+n=h@j01&ew+us_4#)i8zk3p7)o2tkh8@p$334&5qt#z1fg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mongolog',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'mongolog.middleware.RequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mongolog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mongolog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
