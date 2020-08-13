'''
        settings.py
   @ Author  Kuntal
   @ Company 
   @ version  0.1
   @date      10/12/2019
'''

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^a+7&r+fgut4itkgkw=hql!fnu#c(-26bo=w%w9z-wa=xn%&&8'
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application INSTALLED Apps List 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',              # <-- CORS
    'rest_framework',
    'App',
]

# Application MIDDLEWARE List
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',        # <-- CORS
    'django.middleware.common.CommonMiddleware',    # <-- CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',   # <-- Message DJango
    # 'django.middleware.cache.UpdateCacheMiddleware',    # <-- Cache
    # 'django.middleware.common.CommonMiddleware',    # <-- Cache
    # 'django.middleware.cache.FetchFromCacheMiddleware',    # <-- Cache
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BlankSetup.urls'

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
                'django.contrib.messages.context_processors.messages',  # <-- Message DJango
            ],
        },
    },
]

WSGI_APPLICATION = 'BlankSetup.wsgi.application'

# Database Default
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Database Postgresql
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}'''

# Database Mongodb
'''DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'ENFORCE_SCHEMA': True,
            'NAME': 'mydatabase',
            'HOST': 'localhost',
            'PORT': 27017
            # 'USER': 'db-username',
            # 'PASSWORD': 'mypassword',
            # 'AUTH_SOURCE': 'db-name',
            # 'AUTH_MECHANISM': 'SCRAM-SHA-1',
            # 'REPLICASET': 'replicaset',
            # 'SSL': 'ssl',
            # 'SSL_CERTFILE': 'ssl_certfile',
            # 'SSL_CA_CERTS': 'ssl_ca_certs',
            # 'READ_PREFERENCE': 'read_preference'
        }
    }'''


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
DEFAULT_IMAGE_PATH = 'default/Image/avater.jpeg'


# CORS Setup Django
'''CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000"
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]'''


# Django Core Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mail@mail.com'
EMAIL_HOST_PASSWORD = 'mailpassword'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587


'''REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}'''


'''REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}'''


# Cache Setting
'''SESSION_ENGINE = "django.contrib.sessions.backends.cache"   # <-- Cached Sessions'''

'''CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}'''

'''
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
'''


print("\n", "#"*75, "\n                    \
    Hey Starting Your Server            \
    \n", "#"*75, "\n\n")
