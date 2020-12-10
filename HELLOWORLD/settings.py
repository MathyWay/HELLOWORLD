import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+d%#eyq8zqqi7-b_tq2z4xe7nfsixuao34c0o^%8)#swqz_gwr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HELLOWORLD.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
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

WSGI_APPLICATION = 'HELLOWORLD.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS users (name text not null, password text not null)"""
INSERT_USER_SQL = 'INSERT INTO users (name, password) values (?, ?)'
DELETE_USER_SQL = 'DELETE from users where rowid = (?) and name = (?)'
SELECT_USER_SQL = 'SELECT name from users where rowid = (?)'
CHECK_USER_SQL = 'SELECT rowid, name, password from users where name = (?) and password = (?)'

CREATE_MESSAGE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS mes{} (idfriend text not null,
                                                        messagetype text, message text)"""
SEND_MESSAGE_SQL = 'INSERT INTO mes{} values (?, ?, ?)'
SHOW_MESSAGES_SQL = 'SELECT message, messagetype from mes{} where idfriend = (?)'
MESSAGE_BASE = 'messagebase.db'

INIT_FRIENDS_TABLE_SQL = """CREATE TABLE IF NOT EXISTS fri{} (idfriend int not null, friendname text not null)"""
ADD_FRIEND_SQL = 'INSERT INTO fri{} values (?,?)'
DELETE_FRIEND_SQL = 'DELETE FROM fri{} where idfriend = (?)'
SELECT_FRIENDS_SQL = 'SELECT idfriend, friendname FROM fri{}'
FRIENDS_BASE = 'friendsbase.db'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
