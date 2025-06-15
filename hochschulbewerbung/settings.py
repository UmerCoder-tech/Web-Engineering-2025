from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = "django-insecure-)0ds4$=)kkp%z9ttav^d47a#fhd=mah7&#87v_2!@9yv%4-w^7"
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
    "frontend",  # ✅ dein aktives App-Verzeichnis
]

AUTH_USER_MODEL = 'frontend.StudentUser'  # ✅ Benutzerdefiniertes User Model

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hochschulbewerbung.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # du kannst hier z.B. BASE_DIR / "templates" hinzufügen bei Bedarf
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

WSGI_APPLICATION = "hochschulbewerbung.wsgi.application"
"""""
# Datenbank
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bewerbung_neu',  # <--- HIER geändert
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'unix_socket': '/tmp/mysql.sock',
        }
    }
}
"""

import platform

IS_WINDOWS = platform.system() == 'Windows'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bewerbung_neu',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {} if IS_WINDOWS else {
            'unix_socket': '/tmp/mysql.sock'
        },
    }
}

# Passwort-Validierung
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

# Internationalisierung
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Statische Dateien
STATIC_URL = "static/"

# Primärschlüssel-Standard
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Nach Login weiterleiten
LOGIN_REDIRECT_URL = '/dashboard/'

# 🔐 Authentifizierungs-Backends
AUTHENTICATION_BACKENDS = [
    #'frontend.backends.UsernameOrEmailBackend',  # ✅ korrigiert
    'django.contrib.auth.backends.ModelBackend',  # Standard fallback
]
