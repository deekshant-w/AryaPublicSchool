from pathlib import Path
import os
from google.oauth2 import service_account
import json
import base64
import dj_database_url
from django.test.runner import DiscoverRunner
from pathlib import Path

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration
#
# sentry_sdk.init(
#     dsn="https://9c2f70e7fa1248b0ab2118bae39b62cc@o540354.ingest.sentry.io/5658550",
#     integrations=[DjangoIntegration()],
#     traces_sample_rate=1.0,
#
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("APS_SECRET_KEY") or 'cy+tw^b@!&pby40n+0yvw87q19!rk0cb(%1=sh7!r5hbajrp4b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
IS_HEROKU = "DYNO" in os.environ

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'main',
    'tinymce',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AryaPublicSchool.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            './templates'
        ],
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

WSGI_APPLICATION = 'AryaPublicSchool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if 'AIVEN' in os.environ:
    # Aiven PostgreSQL
    print("Aiven online!")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("AIVEN_NAME"),
            'USER': os.getenv("AIVEN_USER"),
            'PASSWORD': os.getenv("AIVEN_PASSWORD"),
            'HOST': os.getenv("AIVEN_HOST"),
            'PORT': os.getenv("AIVEN_PORT"),
        }
    }
else:
    # Load from local file
    aivevn_file = "../aiven.json"
    print("Loading Aiven config from file: " + aivevn_file)
    aiven_config = json.loads(open(aivevn_file).read())
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': aiven_config["AIVEN_NAME"],
            'USER': aiven_config["AIVEN_USER"],
            'PASSWORD': aiven_config["AIVEN_PASSWORD"],
            'HOST': aiven_config["AIVEN_HOST"],
            'PORT': aiven_config["AIVEN_PORT"],
        }
    }


# Heroku Postgress
# MAX_CONN_AGE = 600
# if "DATABASE_URL" in os.environ:
#     # Configure Django for DATABASE_URL environment variable.
#     DATABASES["default"] = dj_database_url.config(
#         conn_max_age=MAX_CONN_AGE, ssl_require=True)
#     # Enable test database if found in CI environment.
#     if "CI" in os.environ:
#         DATABASES["default"]["TEST"] = DATABASES["default"]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

class HerokuDiscoverRunner(DiscoverRunner):
    """Test Runner for Heroku CI, which provides a database for you.
    This requires you to set the TEST database (done for you by settings().)"""

    def setup_databases(self, **kwargs):
        self.keepdb = True
        return super(HerokuDiscoverRunner, self).setup_databases(**kwargs)

# firebase data storage
# PRODUCTION SETTINGS
if(os.getenv("FIREBASE_JSON")):
    GS_CREDENTIALS = service_account.Credentials.from_service_account_info(json.loads(base64.b64decode(os.environ.get("FIREBASE_JSON")).decode()))

# DEVELOPMENT SETTINGS
# place the file one directory up of manage.py
else:
    try:
        GS_CREDENTIALS = service_account.Credentials.from_service_account_file(r"..\arya-public-school-web-firebase-adminsdk-zcad0-a095058cfe.json")
    except Exception as e:
        print("ERR-FIREBASE-JSON",e)

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'arya-public-school-web.appspot.com'
GS_DEFAULT_ACL = "publicRead"

# tinyMCE
DJANGO_SETTINGS_MODULE='testtinymce.settings'
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'height' : "480",
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    'mode': "exact",
}
TINYMCE_SPELLCHECKER = True
TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'
TINYMCE_COMPRESSOR = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
