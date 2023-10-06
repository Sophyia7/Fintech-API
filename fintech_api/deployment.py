import os 
from .settings import *
from .settings import BASE_DIR

# Define URLs that can be allowed to access the backend
ALLOWED_URLS = [os.environ['HOSTNAME']]
CRSF_TRUSTED_ORIGINS = ['https://' + os.environ['HOSTNAME']]
DEBUG = True

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  "corsheaders.middleware.CorsMiddleware",
  "django.middleware.common.CommonMiddleware",
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# connection_string = os.environ['ZURE_CONNECTIONSTRING']
# parameters = {pair.split(':')[0]: pair.split(':')[1] for pair in connection_string.split(';')}


DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.environ['DB_NAME'],
    'USER': os.environ['DB_USER'],
    'PASSWORD': os.environ['DB_PASSWORD'],
    'HOST': os.environ['DB_HOST'],
    'PORT': os.environ['DB_PORT'],
  }
}