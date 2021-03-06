try:
    from settings import *
except ImportError, e:
    pass


import dj_database_url
DATABASES['default'] = dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


DEBUG = TEMPLATE_DEBUG = False
ALLOWED_HOSTS=['*']