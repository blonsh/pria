from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Desactivar DEBUG para mejorar rendimiento

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'pria_dev'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'OPTIONS': {
            'sslmode': 'disable',
        },
        'CONN_MAX_AGE': 0,  # Desactivar pooling de conexiones
    }
}

# Configuración de correo para desarrollo
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configuración de caché para desarrollo
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 300,  # 5 minutos
    }
}

# Desactivar middlewares innecesarios
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Desactivar la toolbar de desarrollo
INSTALLED_APPS = [
    app for app in INSTALLED_APPS if app != 'debug_toolbar'
]

# Desactivar logging detallado
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

# Configuración de depuración
INTERNAL_IPS = [
    '127.0.0.1',
]

# Configuración de archivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Configuración de seguridad para desarrollo
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Configuración de logs para desarrollo
LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['asistencia']['level'] = 'DEBUG'

# Configuración de CORS para desarrollo
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Configuración de API REST para desarrollo
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = [
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.TokenAuthentication',
]

# Configuración de cache para desarrollo
CACHE_MIDDLEWARE_SECONDS = 60
CACHE_MIDDLEWARE_KEY_PREFIX = 'dev_'
