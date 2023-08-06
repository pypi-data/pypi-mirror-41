# Django settings for django_th project.
import os
from django.urls import reverse_lazy

import environ

ROOT_DIR = environ.Path(__file__) - 1
APPS_DIR = ROOT_DIR.path('django_th')

env = environ.Env()
env_file = str(ROOT_DIR.path('.env'))
# print('Loading : {}'.format(env_file))
env.read_env(env_file)
# print('The .env file has been loaded. See settings.py for more information')

DEBUG = env.bool('DEBUG', default=False),  # set to False when using in production
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env.str('DB_NAME', default=BASE_DIR + '/trigger_happy.sqlite3'),
        'USER': env.str('DB_USER', default=''),
        'PASSWORD': env.str('DB_PASSWORD', default=''),
        'HOST': env.str('DB_HOST', default=''),
        'PORT': env.str('DB_PORT', default=''),
    },
    'TEST': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/test_trigger_happy.sqlite3',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = env.str('TIME_ZONE', default='Europe/Paris')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = env.str('LANGUAGE_CODE', default='en')

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = env.bool('USE_I18N', default=True)

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = env.bool('USE_L10N', default=True)

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = env.bool('USE_TZ', default=True)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_th.urls'

# Python dotted path to the WSGI application used by Django's runserver.'
WSGI_APPLICATION = 'django_th.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    # or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'formtools',
    'django_js_reverse',
    'rest_framework',
    'django_th',
    'th_rss',
    # uncomment the lines to enable the service you need
    'th_evernote',
    'th_github',
    'th_joplin',
    'th_mastodon',
    'th_pelican',
    'th_pocket',
    'th_pushbullet',
    'th_reddit',
    'th_slack',
    'th_taiga',
    'th_todoist',
    'th_trello',
    'th_tumblr',
    'th_twitter',
    'th_wallabag',

)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors':
                ["django.contrib.auth.context_processors.auth",
                 # "django.core.context_processors.request",
                 "django.template.context_processors.debug",
                 "django.template.context_processors.i18n",
                 "django.template.context_processors.media",
                 "django.template.context_processors.static",
                 "django.template.context_processors.tz",
                 "django.contrib.messages.context_processors.messages"]
        }
    },
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
                '%(asctime)s %(levelname)s %(module)s %(process)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + '/trigger_happy.log',
            'maxBytes': 61280,
            'backupCount': 3,
            'formatter': 'verbose',

        },
    },
    'loggers':
    {
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_th.trigger_happy': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        }
    }
}

# go back on home page after logged in
LOGIN_REDIRECT_URL = reverse_lazy('base')

CACHES = {
    'default':
    {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR + '/cache/',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    },
    'redis-cache':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "MAX_ENTRIES": 5000,
        }
    },
    'django_th':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "MAX_ENTRIES": 5000,
        }
    },
}

SECRET_KEY = env.str('SECRET_KEY', default='to be defined :P')

TEST_RUNNER = 'django_th.runner.DiscoverRunnerTriggerHappy'
# Unit Test are buggy for this app ; so do not make them
TEST_RUNNER_WHITELIST = ('oauth2_provider', 'corsheaders')

LOGOUT_REDIRECT_URL = '/th/'
