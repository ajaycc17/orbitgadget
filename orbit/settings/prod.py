from .base import *

# Secret key
with open('/home/ajay/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

# Debug in production
DEBUG = False
ALLOWED_HOSTS = ['159.203.90.186', 'localhost',
                 'orbitgadget.com', 'www.orbitgadget.com']

# Installed apps
INSTALLED_APPS += [
    'storages',
]

# Site ID
SITE_ID = 2

# Database variables
with open('/home/ajay/db_name.txt') as a:
    db_name = a.read().strip()

with open('/home/ajay/db_user.txt') as b:
    db_user = b.read().strip()

with open('/home/ajay/db_pass.txt') as c:
    db_pass = c.read().strip()

# Production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_pass,
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Static and media URL on local settings
# STATIC_URL = '/static/'
# MEDIA_URL =  '/media/'

# Static and media files on custom storage
with open('/home/ajay/aws_access_key.txt') as d:
    AWS_ACCESS_KEY_ID = d.read().strip()

with open('/home/ajay/aws_secret_key.txt') as e:
    AWS_SECRET_ACCESS_KEY = e.read().strip()

AWS_STORAGE_BUCKET_NAME = 'orbitfiles'
AWS_S3_ENDPOINT_URL = 'https://orbitfiles.nyc3.digitaloceanspaces.com'
AWS_S3_CUSTOM_DOMAIN = 'api.orbitgadget.com/orbitfiles'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_SIGNATURE_VERSION = 's3v4'

# Static and media URL - with custom domain for CDN
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, 'staticfiles')
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, 'mediafiles')

# Static and media URL - without custom domain for CDN
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, 'staticfiles')
# MEDIA_URL =  'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, 'mediafiles')

# Storage
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# Production recaptcha
with open('/home/ajay/recaptcha_key.txt') as g:
    GOOGLE_RECAPTCHA_SECRET_KEY = g.read().strip()

# Production SMTP Configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'orbitgadget@gmail.com'
# email password
with open('/home/ajay/email_pass.txt') as h:
    EMAIL_HOST_PASSWORD = h.read().strip()

# SSL settings - enable after installing ssl certificate
# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# oauth
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP': {
            'client_id': '680294717219-lu3n2hvlj6j0pfmk67oseblvdp6asreq.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}