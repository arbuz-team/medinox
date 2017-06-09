import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SERVER_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(SERVER_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eunq8#$v(#15yjrd1rip6a=-vech-ptmpxq+_zqoa&n(vr5%k@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.sites', # For include sites
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'nocaptcha_recaptcha',
    'django_countries',

    'server.arbuz',
    'server.main',
    'server.session',
    'server.statement',
    'server.user',
    'server.root',
    'server.sender',
    'server.product',
    'server.catalog',
    'server.translator',
    'server.setting',
    'server.searcher',
    'server.dialog',
    'server.cart',
    'server.navigation',
    'server.payment',
    'server.user.account',
    'server.pdf',

)

MIDDLEWARE_CLASSES = [
    'subdomains.middleware.SubdomainURLRoutingMiddleware', # Subdomain package
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1
ROOT_URLCONF = 'server.arbuz.urls.en'

SUBDOMAIN_URLCONFS = {
    None: 'server.arbuz.urls.en',
    'en': 'server.arbuz.urls.en',
    'pl': 'server.arbuz.urls.pl',
    'de': 'server.arbuz.urls.de',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'client/plugins'),
            os.path.join(BASE_DIR, 'html'),
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

WSGI_APPLICATION = 'server.arbuz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'medinox',
        'USER':     'medinox',
        'PASSWORD': 'szczypiorek&medinox',
        'HOST':     'localhost',
        'PORT':     '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us' # pl/de/en-us

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'client', 'static', 'root')
STATIC_URL = '/_static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'client', 'static', 'tmp')
MEDIA_URL = '/_static/tmp/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'client', 'static'),
)


SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_PASSWORD = 'szczypior7ARBUZ'
EMAIL_HOST_USER = 'sender@arbuz.team'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# captcha
NORECAPTCHA_SITE_KEY = '6LdReA4UAAAAABoCBT6FhqIymqhKwcxxen6hoGdX'
NORECAPTCHA_SECRET_KEY = '6LdReA4UAAAAADIOtRNxLsY0JkaBCfn7w1DKIJs0'

# geoip2
GEOIP_PATH = os.path.join(SERVER_DIR, 'arbuz', 'geoip')

# Payments
PAYPAL_RECEIVER_EMAIL = '93.endo-facilitator@gmail.com'
DOTPAY_RECEIVER_ID = '732547'

# Root email
ROOT_EMAIL = '93.endo@gmail.com'

# Other
SESSION_SAVE_EVERY_REQUEST = True
DISPLAY_STATUS = True
