"""Production settings and globals."""


from os import environ
import dj_database_url
# from S3 import CallingFormat

from base import *


# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

INSTALLED_APPS += ('gunicorn',)

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')
if not EMAIL_HOST:
    EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.sendgrid.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')
if not EMAIL_HOST_PASSWORD:
    EMAIL_HOST_PASSWORD = environ.get('SENDGRID_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', '')
if not EMAIL_HOST_USER:
    EMAIL_HOST_USER = environ.get('SENDGRID_USERNAME', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {'default': dj_database_url.config()}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {}
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION


########## STORAGE
# INSTALLED_APPS += ('storages',)
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# AWS_ACCESS_KEY_ID = get_env_setting('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = get_env_setting('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = "shortener"
#
# AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
# AWS_HEADERS = {
#     'Expires': 'Thu, 15 Apr 2020 20:00:00 GMT',
#     'Cache-Control': 'max-age=86400',
# }
# AWS_QUERYSTRING_AUTH = False

# STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = STATIC_URL
########## END STORAGE

########### LOGGING
# Emails site admin when 500 is triggered
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logutils.colorize.ColorizingStreamHandler',
            'formatter': 'standard'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', ],
            'propagate': True,
            'level': 'ERROR',
        },
        'django.request': {

            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        '': {
            'handlers': ['console', ],
            'level': environ.get('DEBUG_LEVEL', 'ERROR'),
        },
    }
}
########### END LOGGING

########### HOSTS
ALLOWED_HOSTS = ['2scoops.co', 'twoscoops-co.herokuapp.com', 'www.2scoops.co', 'twoscoops-co2.herokuapp.com', ]
########### END HOSTS
