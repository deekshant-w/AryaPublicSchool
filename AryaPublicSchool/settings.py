from pathlib import Path
import os
from google.oauth2 import service_account
import json
import base64
import dj_database_url  # NOTE: possibly unwanted — only used by the commented-out Heroku Postgres block below
from django.test.runner import DiscoverRunner
from pathlib import Path
from aiven.client import AivenClient
import time

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
    AIVEN_CLI = {
        "PROJECT": os.getenv("AIVEN_PROJECT"),
        "SERVICE": os.getenv("AIVEN_SERVICE"),
        "TOKEN": os.getenv("AIVEN_CLI_TOKEN"),
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
    AIVEN_CLI = {
        "PROJECT": aiven_config["AIVEN_PROJECT"],
        "SERVICE": aiven_config["AIVEN_SERVICE"],
        "TOKEN": aiven_config["AIVEN_CLI_TOKEN"],
    }

# Turn ON Aiven
def turnOnAiven(restart=False):
    TRIES = 3
    POOL_TIME = 60
    WAIT_TIME = 5

    for _ in range(TRIES):
        print("Attempting to turn on Aiven... Attempt", _+1)
        try:
            client = AivenClient("https://api.aiven.io")
            client.set_auth_token(AIVEN_CLI["TOKEN"])
            if client.get_service(project=AIVEN_CLI["PROJECT"], service=AIVEN_CLI["SERVICE"])["state"].upper() == "RUNNING" and not restart:
                print("Aiven is already ON!")
                return
            client.update_service(project=AIVEN_CLI["PROJECT"], service=AIVEN_CLI["SERVICE"], powered=True)
        except Exception as e:
            print("Error turning on Aiven:", e)
            raise e
        
        if restart:
            client.update_service(project=AIVEN_CLI["PROJECT"], service=AIVEN_CLI["SERVICE"], powered=False)
            restart_wait_start_time = time.time()
            while time.time() - restart_wait_start_time < POOL_TIME:
                try:
                    state = client.get_service(project=AIVEN_CLI["PROJECT"], service=AIVEN_CLI["SERVICE"])
                    if state["state"].upper() == "POWEROFF":
                        print("Aiven is OFF! Restarting...")
                        break
                    else:
                        print("Waiting for Aiven to turn off... Current state:", state["state"])
                        time.sleep(1)
                except Exception as e:
                    print("Error checking Aiven state:", e)
                    time.sleep(WAIT_TIME)
            time.sleep(WAIT_TIME)  # Wait a bit before trying to turn it on again
        
        start_time = time.time()
        while time.time() - start_time < POOL_TIME:
            try:
                state = client.get_service(project=AIVEN_CLI["PROJECT"], service=AIVEN_CLI["SERVICE"])
                if state["state"].upper() == "RUNNING":
                    print("Aiven is ON!")
                    time.sleep(WAIT_TIME)  # Wait a bit to ensure it's fully up before returning
                    return
                else:
                    print("Waiting for Aiven to turn on... Current state:", state["state"])
                    time.sleep(WAIT_TIME)
            except Exception as e:
                print("Error checking Aiven state:", e)
                time.sleep(WAIT_TIME)
    raise Exception("Failed to load the secret sauce. Please try again in a few minutes 😿🙏🏻")
turnOnAiven()
                

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
    print("FIREBASE JSON LOADED FROM ENV VARIABLE")

# DEVELOPMENT SETTINGS
# place the file one directory up of manage.py
else:
    try:
        GS_CREDENTIALS = service_account.Credentials.from_service_account_file(r"..\arya-public-school-web-firebase-adminsdk-zcad0-75bad95d22.json")
        print("FIREBASE JSON LOADED FROM FILE")
    except Exception as e:
        GS_CREDENTIALS = None
        print("ERR-FIREBASE-JSON",e)

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'arya-public-school-web.appspot.com'
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": GS_BUCKET_NAME,
            "default_acl": "publicRead",
            "credentials": GS_CREDENTIALS,
        },
    },
    "staticfiles": {
        # Keep static files local (standard setup)
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        # OR if you want static files on Firebase too:
        # "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        # "OPTIONS": {
        #     "bucket_name": GS_BUCKET_NAME,
        #     "location": "static",
        # },
    },
}
MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'

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
TINYMCE_COMPRESSOR = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
