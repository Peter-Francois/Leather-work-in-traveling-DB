"""
Django settings for web_shop project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import environ
import os
from django.conf import settings
from django.utils.translation import gettext_lazy as _




env = environ.Env(
    DEBUG=(bool, False)  # Par défaut, DEBUG sera False
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Path(__file__).resolve().parent.parent

# Lisez le fichier .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'page_vente.apps.PageVenteConfig',
    'cloudinary',
    'cloudinary_storage',
    'csp',
    'django.contrib.sitemaps',
    'django_extensions',
]


LANGUAGES = [
    ('fr', _('Français')),
    ('en', _('English')),
]

LANGUAGE_CODE = 'fr'  # Langue par défaut

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'web_shop.middleware.BlockWordPressRequestsMiddleware',
]

ROOT_URLCONF = 'web_shop.urls'

CLIENT_PHONE_NUMBER = env('CLIENT_PHONE_NUMBER', default='Non disponible')
CLIENT_EMAIL=env('CLIENT_EMAIL',default='Non disponible')
CLIENT_INSTAGRAM = env('CLIENT_INSTAGRAM', default='Non disponible')
CLIENT_FACEBOOK = env('CLIENT_FACEBOOK', default='Non disponible')

def global_variables(request):
    return {
        'CLIENT_PHONE_NUMBER': settings.CLIENT_PHONE_NUMBER,
        'CLIENT_EMAIL': settings.CLIENT_EMAIL,
        'CLIENT_INSTAGRAM': settings.CLIENT_INSTAGRAM,
        'CLIENT_FACEBOOK': settings.CLIENT_FACEBOOK,
    }
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
                'web_shop.settings.global_variables', # rendre les variables de .env disponibles dans les templates
            ],
        },
    },
]

WSGI_APPLICATION = 'web_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': env.db(),


}

CACHES = {
    'default': {
         # Config en dev
        'BACKEND': env('CACHE_BACKEND'), # last config with pymemecache that don't work for pythonanywhere
        'LOCATION': env('CACHE_LOCATION'), # last config with pymemecache that don't work for pythonanywhere

        # Config en production
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': '/home/ton_utilisateur/django_cache',  Remplace par ton dossier sur PythonAnywhere
        # 'TIMEOUT': 300,  # 5 minutes (ajuste selon tes besoins)
        # 'OPTIONS': {
        #     'MAX_ENTRIES': 1000  # Nombre max d'entrées en cache
        # }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Dossier où Django va collecter les fichiers statiques
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'page_vente/static'),  # Dossier où tu mets tes fichiers statiques
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'  # Peut permettre certaines interactions externes
SECURE_CROSS_ORIGIN_RESOURCE_POLICY = 'same-origin'  # Permet de charger des ressources locales

if env('DJANGO_ENV') == 'development':
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_SECONDS = 0
    SESSION_COOKIE_SAMESITE = 'Lax' #ne permet pas les cookies cross-site
    CSRF_COOKIE_SAMESITE = 'Lax' #ne permet pas les cookies cross-site
    SECURE_REFERRER_POLICY = 'strict-origin'  # Envoie uniquement l'origine du site pour les requêtes sécurisées
    SECURE_CONTENT_TYPE_NOSNIFF = False  # Moins restrictif pendant le développement pour faciliter les tests
    CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'","http://localhost:*", "ws://localhost:*", "http://127.0.0.1")
    CSP_IMG_SRC = ("'self'", "https://res.cloudinary.com")
else:
    # Pour la production (avec HTTPS)
    SESSION_COOKIE_SECURE = True  # Assure que les cookies de session ne sont envoyés qu'en HTTPS
    CSRF_COOKIE_SECURE = True     # Assure que le cookie CSRF est aussi sécurisé
    SESSION_COOKIE_SAMESITE = 'Lax' #ne permet pas les cookies cross-site
    CSRF_COOKIE_SAMESITE = 'Lax' #ne permet pas les cookies cross-site
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000    # Active HTTP Strict Transport Security (1 an)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_REFERRER_POLICY = 'strict-origin'  # Envoie uniquement l'origine du site pour les requêtes sécurisées
    SECURE_CONTENT_TYPE_NOSNIFF = True  # Empêche la détection incorrecte des types MIME
    CSP_DEFAULT_SRC = ("'self'",)
    CSP_SCRIPT_SRC = ("'self'",)
    CSP_IMG_SRC = ("'self'", "https://res.cloudinary.com")

SECURE_BROWSER_XSS_FILTER = True  # Protège contre les attaques XSS
CSRF_COOKIE_HTTPONLY = True  # Empêche l'accès au cookie CSRF depuis le client
X_FRAME_OPTIONS = 'DENY'


import cloudinary
# Cloudinary configuration

cloudinary.config(
    cloud_name = env('CLOUDINARY_CLOUD_NAME'),
    api_key = env('CLOUDINARY_API_KEY'),
    api_secret = env('CLOUDINARY_API_SECRET'),
    secure = True,
    upload_preset=env('CLOUDINARY_UPLOAD_PRESET'),
    analytics=False,
)

# Configurer le proxy sur PythonAnywhere uniquement
if 'PYTHONANYWHERE_DOMAIN' in os.environ:
    cloudinary.config(api_proxy='http://proxy.server:3128')
else:
    pass

import cloudinary.uploader
import cloudinary.api


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Stripe configuration
STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = env('STRIPE_WEBHOOK_SECRET')

# Mail configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Configuration SMTP
EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env.int("EMAIL_PORT")
EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("EMAIL_HOST_USER")