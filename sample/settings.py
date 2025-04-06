import os
from pathlib import Path
from mongoengine import connect

BASE_DIR = Path(__file__).resolve().parent.parent

# MongoDB connection
from urllib.parse import quote_plus

username = "reddykumbamsathwik"
password = quote_plus("Sathwikreddy@12")  # This safely escapes special characters
uri = f"mongodb+srv://{username}:{password}@sample.cbtw0ln.mongodb.net/?retryWrites=true&w=majority&appName=Sample"

connect(
    db='mydb',
    host=uri,
    port=27017
)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bw&c*6hx4typmoshw-5ao!p12f^ce(q-m&e@wr=5=jkqkokxze'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myfirstapp',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ensure you have a 'templates' directory
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

# ✅ Corrected MIDDLEWARE (WhiteNoise added here directly)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 👈 Add this here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ Static files settings for Render
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
