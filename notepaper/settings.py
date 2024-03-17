from pathlib import Path
import json
BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = "dfopufgiosdyrht7439v42n90674*(y*pYH89q*ioyr8oiqwe;Ytruehau8i^F*RAYH5ERIFEYA68RYHiqahIOy8oi3qhyiow&(OIr357r9oea:Y*OIy3q5y89))"

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework.authtoken",
    "rest_framework",
    "paperapi",
    "website",
    "errorhandler",
    "webapi",
    "UserAPI"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "notepaper.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "notepaper.wsgi.application"




DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS":{"read_default_file":"maria.cnf"},
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK={
    'DEFAULT_RENDERER_CLASSES':[
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.authentication.TokenAuthentication'
    ]
}

DATA_UPLOAD_MAX_NUMBER_FILES=500


with open("email.json",'r') as email:
    emailJson = json.load(email)


EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = emailJson.get('email')
EMAIL_HOST_PASSWORD = emailJson.get('password')
DEFAULT_FROM_EMAIL = emailJson.get('email')
