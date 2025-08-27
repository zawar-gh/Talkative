import os
from pathlib import Path


# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET KEY
SECRET_KEY = '!1223334444$'

# DEBUG
DEBUG = True  # Turn False in production


# ALLOWED HOSTS
ALLOWED_HOSTS = ['192.168.13.1', '127.0.0.1','localhost']

# INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',  # optional if mobile app needs API access

    # Local apps
    'contacts',  # we will create this app later
]

# MIDDLEWARE
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # must be at top if using CORS
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # optional for static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL CONFIGURATION
ROOT_URLCONF = 'backend.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # optional for admin or custom templates
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

# WSGI / ASGI APPLICATION
WSGI_APPLICATION = 'backend.wsgi.application'
ASGI_APPLICATION = 'backend.asgi.application'  # optional if using async later

# DATABASE CONFIGURATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "talkative_db",
        "USER": "talkative_user",
        "PASSWORD": "SecurePass123",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']  # optional if you have custom static files

# MEDIA FILES
MEDIA_URL = '/media/'  # URL path for media files
MEDIA_ROOT = BASE_DIR / 'media' # Folder where uploaded files will be stored

# CORS 
CORS_ALLOW_ALL_ORIGINS = True  # only for development

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # for testing, change in production
    ]
}

# DEFAULT AUTO FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
