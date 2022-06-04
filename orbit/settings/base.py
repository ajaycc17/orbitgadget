from pathlib import Path
from django.contrib.messages import constants as messages

# BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# print("base dir path", BASE_DIR)

# Application definition
INSTALLED_APPS = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'blog.apps.BlogConfig',
    'project.apps.ProjectConfig',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'tailwind',
    'theme',
    'tinymce',
    # 'cachalot',
]

# tailwind
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]

LOGIN_REDIRECT_URL = '/'

# npm
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'orbit.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

# WSGI application
WSGI_APPLICATION = 'orbit.wsgi.application'

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static DIR
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Static and media files hosting locally
# import os
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Message tags
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# tinymce
TINYMCE_COMPRESSOR = False
# TINYMCE_JS_ROOT = os.path.join(STATICFILES_DIRS[0], "tinymce")
TINYMCE_DEFAULT_CONFIG = {
    "height": "550px",
    "referrer_policy": 'origin',
    "menubar": "file edit view insert format tools table help",
    "plugins": 
            "advlist autolink lists link image charmap print preview hr anchor pagebreak searchreplace wordcount visualblocks visualchars code codesample fullscreen insertdatetime media nonbreaking table emoticons template paste help quickbars toc",
    "toolbar":
            "undo redo | toc | styleselect | codesample | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist fullscreen | link image | print preview media outdent indent | forecolor backcolor emoticons | help",
    "custom_undo_redo_levels": 10,
    "codesample_languages": [
        { "text": 'HTML/XML', "value": 'markup' },
        { "text": 'JavaScript', "value": 'javascript' },
        { "text": 'CSS', "value": 'css' },
        { "text": 'PHP', "value": 'php' },
        { "text": 'Ruby', "value": 'ruby' },
        { "text": 'Python', "value": 'python' },
        { "text": 'Java', "value": 'java' },
        { "text": 'C', "value": 'c' },
        { "text": 'C#', "value": 'csharp' },
        { "text": 'C++', "value": 'cpp' },
        { "text": 'Shell', "value": 'shell' },
        { "text": 'Arduino', "value": 'arduino' },
        { "text": 'ASP.NET', "value": 'aspnet' },
        { "text": 'Djano/Jinja2', "value": 'django' },
        { "text": 'Docker', "value": 'docker' },
        { "text": 'Git', "value": 'git' },
        { "text": 'Go', "value": 'go' },
        { "text": 'MongoDB', "value": 'mongodb' },
        { "text": 'MATLAB', "value": 'matlab' },
        { "text": 'Kotlin', "value": 'kotlin' },
        { "text": 'JSON', "value": 'json' },
        { "text": 'GitIgnore', "value": 'ignore' },
        { "text": 'GraphQL', "value": 'graphql' },
        { "text": 'React JSX', "value": 'jsx' },
        { "text": 'SCSS', "value": 'scss' },
        { "text": 'SQL', "value": 'sql' },
        { "text": 'TypeScript', "value": 'typescript' },
        { "text": 'Vim', "value": 'vim' },
        { "text": 'VHDL', "value": 'vhdl' },
    ],
    "content_css": 'css/content.css',
    "toc_depth": 3,
    "toc_header": 'h3',
    "quickbars_insert_toolbar": 'h2 h3 codesample image table | hr pagebreak',
    "quickbars_selection_toolbar": 'bold italic | formatselect | quicklink formatcode blockquote h2 h3',
    "fullscreen_native": True,
    "link_default_protocol": 'https',
    "default_link_target": '_blank',
    "image_caption": True,
}