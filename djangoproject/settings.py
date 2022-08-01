"""
Django settings for djangoproject project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from os import path, getenv
from dotenv import load_dotenv
import sys
import cloudinary

config = cloudinary.config(secure=True)

import cloudinary.uploader
import cloudinary.api


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'djangogramm-romantsov.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'djangogramm',
    'easy_thumbnails',
    'django_extensions',
    'bootstrap5',
    'django_bootstrap_icons',
    'debug_toolbar',
    'cloudinary',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'djangoproject.urls'

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

WSGI_APPLICATION = 'djangoproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8134r6g2ak6q3',
        'USER': 'nzsxykbbjzgjfz',
        'PASSWORD': getenv('HEROKU_POSTGRES_PASSWORD'),
        'HOST': 'ec2-52-49-120-150.eu-west-1.compute.amazonaws.com',
        'PORT': 5432,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'djangogramm.User'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.ukr.net'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'romantsovdmytro@ukr.net'
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')

AUTHENTICATION_BACKENDS = [
    'djangogramm.utils.EmailBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
]

SOCIAL_AUTH_GITHUB_KEY = 'bb11fa5c23ded0ca092e'
SOCIAL_AUTH_GITHUB_SECRET = getenv('SOCIAL_AUTH_GITHUB_SECRET')

SOCIAL_AUTH_JSONFIELD_ENABLED = True

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/login/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

STATIC_ROOT = path.join(BASE_DIR, 'djangogramm', 'static')

STATICFILES_DIRS = []

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Amazon S3
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


DEFAULT_USER_AVATAR = 'https://res.cloudinary.com/dsc8n66p9/image/upload/v1658503584/avatars/user_icon_msyg0x.png'

INTERNAL_IPS = [
    "127.0.0.1",
]



if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    }

