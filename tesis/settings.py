"""
Django settings for tesis project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-e7tbr9wt0^8pl#u+i)65o&2rf94)o0j!e@+hsgfn+(562_zlno'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-e7tbr9wt0^8pl#u+i)65o&2rf94)o0j!e@+hsgfn+(562_zlno')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

AUTH_USER_MODEL= "users.User"
AUTHENTICATION_BACKENDS= [
    'django.contrib.auth.backends.ModelBackend',
    # "django.contrib.auth.backends.AllowAllUsersModelBackend",
    "users.backends.CaseInsensitiveModelBackend"
    ]
# LOGIN_REDIRECT_URL= "users/view_dashboard"

ALLOWED_HOSTS = ["stark-oasis-79142.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'departamentos.apps.DepartamentosConfig',
    'departamentos_geo.apps.DepartamentosGeoConfig',
    'edificios.apps.EdificiosConfig',
    'equipo.apps.EquipoConfig',
    'unidades.apps.UnidadesConfig',
    'users.apps.UsersConfig',
        
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #for production serving assets in heroku
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tesis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'tesis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    },
    
   # 'default': {
   #     'ENGINE': 'sql_server.pyodbc',
   #     'NAME': 'thesis_project',
   #     'USER': 'thesis',
   #     'PASSWORD': 'toorbot123*',
   #     'HOST': 'thesis-project.database.windows.net',
   #     'PORT': '1433',


   #     'OPTIONS':{
   #         'driver': 'ODBC Driver 17 for SQL Server',
   #     }

   # },

   "multimedia":{
       "ENGINE": "djongo",
       "NAME": "multimedia",
       "USER": "root",
       "PASSWORD": "toorbot123",
       "CLIENT":{
           "HOST": "mongodb+srv://root:toorbot123@cluster0.nzcgo.mongodb.net/test",
           "PORT": "27017",
       }
   }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS= [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
