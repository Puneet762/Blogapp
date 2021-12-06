"""
Django settings for Blog_application project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG_VALUE') == "True")

# To check the site on Mobile and localhost
ALLOWED_HOSTS = ['blog-app-pydj.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'blogs.apps.BlogsConfig',
    'users.apps.UsersConfig',
    'blogs_api.apps.BlogsApiConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup',
    'django.contrib.humanize',
    'storages',
    'ckeditor',
    'rest_framework',
    'ckeditor_uploader',
]


# Makes the API to show only JSON Data
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'width': 'auto',
        'toolbar_Custom': [
            ["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
            ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ["Image", "Table", "Link", "Unlink", "Anchor",
                "SectionLink", "Embed"], ['Undo', 'Redo'], ["CodeSnippet"],
            ["Maximize"]
        ],

        # Remove these dialog tabs (semicolon separated dialog:tab)
        'removeDialogTabs': ';'.join([
            'image:advanced',
            'image:Link',
            'link:upload',
            'table:advanced',
            #'tableProperties:advanced',
            ]),
        
        # Extra plugins to be used in the editor
        'extraPlugins': ','.join([
            'mathjax',  # Used to render mathematical formulae
            'codesnippet',  # Used to add code snippets
            'image2',  # Loads new and better image dialog
            'embed',  # Used for embedding media (YouTube/Slideshare etc)
            'tableresize',  # Used to allow resizing of columns in tables
        ]),
    }

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Blog_application.urls'

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
                'blogs.context_processors.notifications_exist',
            ],
            'libraries':  {
                'dict_key': 'blogs.templatetags.dict_key',
            }
        },
    },
]

WSGI_APPLICATION = 'Blog_application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


# Extra places for collectstatic to find static files.
'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
'''

# Tells cripsy forms to use bootstrap 4
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Tells which page to show when user successfully logs in
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'

# This is the Directory where the Uploaded images are kept on the File System
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'uploads/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

# AWS Credentials
# AWS Credentials
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# If a user uploads an image with a name already existing (that some other user has already uploaded), the image
# will not be overriden [if set to False]
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_ADDRESSING_STYLE = "virtual"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


django_heroku.settings(locals())