import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'r1ien0!)9_q#k!1zt+zx6^g%-lu31se5es4ukyg*5$c^dw1a7u' # must be unique for your project
DEBUG = TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['jameslittle.org', '0.0.0.0'] # must match your site domains
INSTALLED_APPS = (
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
ROOT_URLCONF = 'portfolio.urls'
WSGI_APPLICATION = 'portfolio.wsgi.application'
STATIC_URL = '/static/'
STATIC_ROOT = 'static'