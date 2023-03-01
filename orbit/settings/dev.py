from .base import *
import os

# Secret key
SECRET_KEY = 'django-insecure-2@je&3s47ffy8ph&k*8l=%ep*8mn0rj0_-b)e9r4ij=j%hqee-'

# Debug in development
DEBUG = True
ALLOWED_HOSTS = []

# Site ID
SITE_ID = 2

# Local database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static URL and DIR
STATIC_URL = '/static/'

# Media Files local
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Local recaptcha
GOOGLE_RECAPTCHA_SECRET_KEY = '6LeleRAaAAAAAEHqQzug3vmGBNg1L605fHS8XYyt'

# Local SMTP Configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'orbitgadget@gmail.com'
# change according to folder structure
# with open('E:/OrbitGadget/credentials/email_pass.txt') as h:
#     EMAIL_HOST_PASSWORD = h.read().strip()
    
# oauth
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP': {
            'client_id': '336781927713-8vqcj9tluh20l4mgclmja9e93d9bdep7.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}