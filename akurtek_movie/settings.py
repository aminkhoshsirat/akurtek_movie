from pathlib import Path

from .config import *

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ib4h63%@ok+b63mgwo(9_yi@z@m13k_^#!qw1nzr(ebpw)^m*%'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'boto3',
    'storages',
    'django_jalali',
    'jalali_date',
    'django_render_partial',
    'azbankgateways',

    'apps.user.apps.UserConfig',
    'apps.blog.apps.BlogConfig',
    'apps.movie.apps.MovieConfig',
    'apps.panel.apps.PanelConfig',
    'apps.notification.apps.NotificationConfig',
    'apps.chat.apps.ChatConfig',
    'apps.payment.apps.PaymentConfig',
]

AUTH_USER_MODEL = 'user.UserModel'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'akurtek_movie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

ASGI_APPLICATION = 'akurtek_movie.asgi.application'

DATABASES = {
    'default': postgres_config
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
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

LANGUAGE_CODE = 'fa-iran'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL CONFIG
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'aminkhoshsirat1381@gmail.com'
EMAIL_HOST_PASSWORD = 'aminkh1110'


# Arvan Storage

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = arvan_cloud_config.get('access_key')

AWS_SECRET_ACCESS_KEY = arvan_cloud_config.get('secret_key')

AWS_S3_ENDPOINT_URL = arvan_cloud_config.get('simin_domain')

AWS_STORAGE_BUCKET_NAME = arvan_cloud_config.get('bucket_name')

AWS_SERVICE_NAME = 's3'

AWS_S3_FILE_OVERWRITE = False

AWS_QUERYSTRING_AUTH = False


AZ_IRANIAN_BANK_GATEWAYS = {
    "GATEWAYS": {
        "BMI": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
            "SECRET_KEY": "<YOUR SECRET CODE>",
        },
        "SEP": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
        },
        "ZARINPAL": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "SANDBOX": 0,  # 0 disable, 1 active
        },
        "IDPAY": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "METHOD": "POST",  # GET or POST
            "X_SANDBOX": 0,  # 0 disable, 1 active
        },
        "ZIBAL": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        },
        "BAHAMTA": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        },
        "MELLAT": {
            "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
            "USERNAME": "<YOUR USERNAME>",
            "PASSWORD": "<YOUR PASSWORD>",
        },
        "PAYV1": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "X_SANDBOX": 0  # 0 disable, 1 active
        },
    },
    "IS_SAMPLE_FORM_ENABLE": True,  # اختیاری و پیش فرض غیر فعال است
    "DEFAULT": "BMI",
    "CURRENCY": "IRR",  # اختیاری
    "TRACKING_CODE_QUERY_PARAM": "tc",  # اختیاری
    "TRACKING_CODE_LENGTH": 16,  # اختیاری
    "SETTING_VALUE_READER_CLASS": "azbankgateways.readers.DefaultReader",  # اختیاری
    "BANK_PRIORITIES": [
        "BMI",
        "SEP",
        # and so on ...
    ],  # اختیاری
    "IS_SAFE_GET_GATEWAY_PAYMENT": False,  # اختیاری، بهتر است True بزارید.
    "CUSTOM_APP": None,  # اختیاری
}
