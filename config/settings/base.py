"""
Base settings to build other settings files upon.
"""
from __future__ import absolute_import, unicode_literals

from pathlib import Path
from django.contrib.messages import constants as messages
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

import environ

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# dropsride/
APPS_DIR = ROOT_DIR / "dropsride"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".enviroments"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Africa/Lagos"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]
LANGUAGES = (
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('it', _('Italian')),
    ('ru', _('Russia')),
)
PARLER_LANGUAGES = {
    None: (
        {'code': 'de',}, # French
        {'code': 'en',}, # English
        {'code': 'es',}, # Spanish
        {'code': 'fr',}, # French
        {'code': 'it',}, # Spanish
        {'code': 'ru',}, # French
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}

# mESSAGE tAGS
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger'
}

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default="postgres:///dropsride",
    ),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = 'config.asgi.application'

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'jet.dashboard',
    'jet',

    "admin_honeypot",

    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.forms",
]
THIRD_PARTY_APPS = [
    'widget_tweaks',
    "crispy_forms",
    "crispy_tailwind",

    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

    # hitcount or view count
    'hitcount',

    # Field color picker
    "colorfield",
    "taggit",

    # table filter with django and alpine
    'django_filters',
    'django_tables2',

    # Emoji picker
    'emoji_picker',

    # Django countries
    'countries_plus',

    # image resize automatic
    'stdimage',

    # language libraries
    'rosetta',
    'parler',


    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",

    # Get User phone details from IP
    'django_user_agents',
    # push notifications settings
    # TODO: alternative way to create push notifications
    # for sending through the backend to users
    'webpush',
    # 'push_notifications',

    # WYSIWYG Editor
    'tinymce',

    # user notifications like facebook
    "notifications",

    # export admin actions to multiple formats
    'import_export',

    "webpack_boilerplate"
]

LOCAL_APPS = [
    "dropsride.users",
    "dropsride.blog",
    "dropsride.promocodes",
    "dropsride.documents",
    "dropsride.companies",
    "dropsride.careers",
    "dropsride.drivers",
    "dropsride.riders",
    "dropsride.admins",
    "dropsride.sitesettings",
    "dropsride.currency"
    # Your stuff: custom apps go here
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "dropsride.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
LOGOUT_REDIRECT_URL = "account_login"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "accounts/login/"
LOGOUT_URL = "accounts/logout/"
LOGIN_EXEMPT_URLS = ["api/users/", "api/drivers/", "api/riders", "api/promos/", "api/admins/", "settings", "mfa", "reset", "users/", "drivers/", "riders/", "admins/", "accounts/"]

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    # HTML Minifying
    "django.middleware.gzip.GZipMiddleware",
    'django.middleware.cache.UpdateCacheMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',

    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # htmx middleware
    "django_htmx.middleware.HtmxMiddleware",

    # custom middlewares
    "dropsride.users.ip_middleware.IpAddressMiddleware",
    # "dropsride.admins.htmx_template_middleware.HtmxResponseMiddleware",
    # "dropsride.users.login_middlewar.LoginRequiredMiddleware",



    'django_user_agents.middleware.UserAgentMiddleware',
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(ROOT_DIR / "frontend/build")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
WEBPACK_LOADER = {
    "MANIFEST_FILE": str(ROOT_DIR / "frontend/build/manifest.json")
}
NPM_BIN_PATH = '/usr/local/bin/npm'

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [str(APPS_DIR / "templates")],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "dropsride.utils.context_processors.context_settings",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "tailwind"
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 1209600
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "SAMEORIGIN"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Jeremiah E. David""", "hello@jeremiahedavid.com"),("""DropsRide""", "noreply@dropsride.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}


# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "email" #username_email or username
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_PRESERVE_USERNAME_CASING = False
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 600
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_OLD_PASSWORD_FIELD_ENABLED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "dropsride.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
ACCOUNT_FORMS = {
    "signup": "dropsride.users.forms.UserSignupForm",
    "login": "dropsride.users.forms.UserLoginForm"
}
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "dropsride.users.adapters.SocialAccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
SOCIALACCOUNT_FORMS = {"signup": "dropsride.users.forms.UserSocialSignupForm"}
SOCIALACCOUNT_QUERY_EMAIL = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile', 'user_friends', 'openid'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name',
            'friends'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',
    }
}

# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"

# By Default swagger ui is available only to admin user(s). You can change permission classes to change that
# See more configuration options at https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings
SPECTACULAR_SETTINGS = {
    "TITLE": "dropsride API",
    "DESCRIPTION": "Documentation of API endpoints of dropsride",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SERVERS": [
        {"url": "http://127.0.0.1:8000", "description": "Local Development server"},
        {"url": "https://dropsride.com", "description": "Production server"},
    ],
}
# Your stuff...
# ------------------------------------------------------------------------------
APPEND_SLASH = True
JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'
JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# tinymce editor
TINY_API = env('TINYMCE_KEY')
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'height': 360,
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
}

# Maximum size, in bytes, of a request before it will be streamed to the
# file system instead of into memory.
FILE_UPLOAD_MAX_MEMORY_SIZE = 26214400000  # i.e. 25.0 MB

# Maximum size in bytes of request data (excluding file uploads) that will be
# read before a SuspiciousOperation (RequestDataTooBig) is raised.
DATA_UPLOAD_MAX_MEMORY_SIZE = 26214400000  # i.e. 2.5 MB

# Maximum number of GET/POST parameters that will be read before a
# SuspiciousOperation (TooManyFieldsSent) is raised.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000
# Number Settings for human readable grouping style and comma
# Decimal separator symbol
DECIMAL_SEPARATOR = "."
# Boolean that sets whether to add thousand separator when formatting numbers
USE_THOUSAND_SEPARATOR = True

# Thousand separator symbol
THOUSAND_SEPARATOR = ","

# Number of digits that will be together, when splitting them by
# THOUSAND_SEPARATOR. 0 means no grouping, 3 means splitting by thousands...
NUMBER_GROUPING = 3

# minifying django HTML Files
HTML_MINIFY = True
EXCLUDE_FROM_MINIFYING = ('^jet/', '^admin/', '^tinymce/', '^filebrowser/', "portal/", "portal/docs/")
KEEP_COMMENTS_ON_MINIFYING = True



# PUSH NOTIFICATIONS
# get vapid keys here https://web-push-codelab.glitch.me/
WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": env("VAPID_PK", default='BCChKvIQPqHUM9Wk2kdatpnMyWtftzRp1u7__kfCR246dupgPdGZg2bcoJ2kMrq494aorqAlKCaMPki6YgLFdcw'),
    "VAPID_PRIVATE_KEY": env("VAPID_SK", default='_-hjzHOEMXvpcEJNRGGJy4qq1giCJZtDWnIST7yiNRo'),
    "VAPID_ADMIN_EMAIL": "push_notification@dropsride.com"
}
PUSH_NOTIFICATIONS_SETTINGS = {
    'WP_CLAIMS': {
        "sub": "mailto: jeremiahedavid@gmail.com"
    },
    'WP_ERROR_TIMEOUT': 10,  # timeout for the request on the push server
    'UPDATE_ON_DUPLICATE_REG_ID': True,
    'APP_SERVER_KEY': env("APP_SK"), #'COPY FROM "vapid --applicationServerKey" command',
    'WP_PRIVATE_KEY': 'private_key.pem', # vapid --gen
}


CSRF_HEADER_NAME="X-CSRFToken"
TAGGIT_CASE_INSENSITIVE = True





# API REQUESTS
MESSENTE_API_USERNAME = env('MESSENTE_USERNAME')
MESSENTE_API_PASSWORD = env('MESSENTE_PASSWORD')
API = env('CURRENCY_EXCHANGE')
URL = env('CURRENCY_EXCHANGE_URL')
FB_ID = env('FACEBOOK_CLIENT_ID')
GOOGLE_API = env('GOOGLE_API_KEY')
GOOGLE_CAPTCHA_SITE_KEY = env('GOOGLE_CAPTCHA_SITE_KEY')
GOOGLE_CAPTCHA_SECRET_KEY = env('GOOGLE_CAPTCHA_SECRET_KEY')
PAYSTACK = env.bool("PAYSTACK_ENABLED", False)
PAYSTACK_TEST_SK = env("PAYSTACK_TEST_SK")
PAYSTACK_TEXT_PK = env("PAYSTACK_TEST_PK")
PAYSTACK_LIVE_SK = env("PAYSTACK_LIVE_SK")
PAYSTACK_LIVE_PK = env("PAYSTACK_LIVE_PK")
PRODUCTION = env.bool("PRODUCTION", False)
BASE_COUNTRY = "NG"
# The default meta precedence order
IPWARE_META_PRECEDENCE_ORDER = (
    'HTTP_X_FORWARDED_FOR', 'X_FORWARDED_FOR',  # <client>, <proxy1>, <proxy2>
    'HTTP_CLIENT_IP',
    'HTTP_X_REAL_IP',
    'HTTP_X_FORWARDED',
    'HTTP_X_CLUSTER_CLIENT_IP',
    'HTTP_FORWARDED_FOR',
    'HTTP_FORWARDED',
    'HTTP_VIA',
    'REMOTE_ADDR',
)

