# Django settings for myuni project.
import os.path
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PATH = os.path.dirname(__file__)

ADMINS = (
     ('Rob Golding', 'rob@goldcs.co.uk'),
     ('Rob Miles', 'robertskmiles@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'myuni'             # Or path to database file if using sqlite3.
DATABASE_USER = 'myuni'             # Not used with sqlite3.
DATABASE_PASSWORD = 'uh5gvx0a'         # Not used with sqlite3.
DATABASE_HOST = 'mysql'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://projects.robgolding.com/media/myuni/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://projects.robgolding.com/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '84qc-oc0f-gm6!evvya3)ddfp)-jt_b$^4v0v1bos!_&95r)0m'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'myuni.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    os.path.join(PATH, '../', 'templates/myuni'),
#    os.path.join(PATH, '../', 'templates'),
    os.path.join(PATH, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"myuni.extras.context_processors.version",
	"myuni.extras.context_processors.current_year"
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'myuni.attachments',
    'myuni.core',
    'myuni.courses',
    'myuni.modules',
    'myuni.account',
    'myuni.people',
    'myuni.schools',
    'myuni.timeperiods',
    'myuni.template',
    'myuni.hexkeys',
    'tagging',
)

#AUTHENTICATION_BACKENDS = (
#    'myuni.auth.backends.CustomUserModelBackend',
#)

MYUNI_EXTRAS_LOCATION = 'myuni.extras'

CUSTOM_USER_MODEL = 'people.Person'

AUTH_PROFILE_MODULE = 'people.Profile'

ROOT_OBJECT = 'object.Object'

REQUIRED_GROUPS_FOR_CONVENERS = ['Staff']
REQUIRED_GROUPS_FOR_LECTURERS = ['Lecturers']
REQUIRED_GROUPS_FOR_TUTORS = ['Tutors']
REQUIRED_GROUPS_FOR_STUDENTS = ['Students']

# Session stuff #
LOGIN_URL = '/account/login'
LOGIN_REDIRECT_URL = '/account/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

try:
	from local_settings import *
except ImportError:
	pass
