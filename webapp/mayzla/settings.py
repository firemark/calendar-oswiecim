import os
import dj_database_url
from django.contrib import messages
from configurations import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Base(Configuration):
    SECRET_KEY = '_@tv!t9s)qgvqd_br_jil+vgyjp$&)=^sa!g-%y=43w83zm$-0'
    ALLOWED_HOSTS = []
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'calendars',
        'sorl.thumbnail',
        'ckeditor',
        'widget_tweaks',
        'datetimewidget',
        'bootstrap3',
        'dbbackup',
        'osm_field',
        'easy_select2',
    )
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )
    ROOT_URLCONF = 'mayzla.urls'
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, './templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'calendars.context_processors.can_add_new_event',
                    'calendars.context_processors.google_analytics',
                ],
            },
        },
    ]
    WSGI_APPLICATION = 'mayzla.wsgi.application'

    LANGUAGE_CODE = 'pl'
    TIME_ZONE = 'Europe/Warsaw'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

    CKEDITOR_CONFIGS = {
        'default': {
            'toolbar': 'Custom',
            'toolbar_Custom': [
                ['Bold', 'Italic', 'Underline'],
                ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                ['Link', 'Unlink'],
                ['RemoveFormat', 'Source']
            ]    },
    }
    CKEDITOR_IMAGE_BACKEND = 'pillow'
    CKEDITOR_UPLOAD_PATH = 'uploadfiles'
    MESSAGE_TAGS = {
        messages.ERROR: 'danger'
    }

    THUMBNAIL_PRESERVE_FORMAT=True

    # We already use jquery in admin, so don't load again
    SELECT2_USE_BUNDLED_JQUERY = False

    # Google Analytics - obtain your tracking ID from GA account
    GOOGLE_ANALYTICS_PROPERTY_ID = ''

class Dev(Base):
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    DBBACKUP_STORAGE_OPTIONS = {'location': '/tmp/'}
    DATABASES = {'default': dj_database_url.config(default='sqlite:///db.sqlite3')}
    DEBUG = True

class Docker(Base):
    STATIC_ROOT = '/static/'
    MEDIA_ROOT = '/media/'
    DBBACKUP_STORAGE_OPTIONS = {'location': '/tmp/'}
    DATABASES = {'default': dj_database_url.config(
        default='postgres://socek:kocham-marka-123@db/socek'
    )}
    DEBUG = True
