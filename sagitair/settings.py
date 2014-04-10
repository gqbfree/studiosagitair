"""
Django settings for sagitair project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ADMINS = (
    ('Orizio Pierangelo', 'pierangelo1982@gmail.com'),
)

MANAGERS = (
    ('Orizio Pierangelo', 'pierangelo1982@gmail.com'),
    ('Orizio Marco', 'orizio.marco@gmail.com'),
)
   

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3+=d22ri8kex%4629ac_(6x_c4gf^0_e$a6o242he)*r1pv5u0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filer',
    'easy_thumbnails',
    'image_cropping',
    'sito',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.contrib.admindocs.middleware.XViewMiddleware',
)



'''
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
'''
'''
CONTEXT_PROCESSORS = (
    #'django.contrib.auth.context_processors.auth',
    #'django.core.context_processors.i18n',
    'django.core.context_processors.csrf',

    )
'''

'''
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.csrf',

    )
'''



ROOT_URLCONF = 'sagitair.urls'

WSGI_APPLICATION = 'sagitair.wsgi.application'

STATIC_ROOT = None

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'sagitair',
        'USER': 'root',
        'PASSWORD': 'alnitek',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'it-IT'

# supported languages
'''
LANGUAGES = (
    ('en', 'English'),
    ('it', 'Italian'),
)
'''
ugettext = lambda s: s

LANGUAGES = (
  ('it', ('Italian')),
  ('en', ('English')),
)

#APPEND_SLASH=False

TIME_ZONE = 'UTC'

USE_I18N = True

# Optional. If you want to use redirects, set this to True
#SOLID_I18N_USE_REDIRECTS = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    #'/home/pierangelo/Scrivania/sagitairbox/sagitair/static/',
)

#STATICFILES_DIRS = ()

STATIC_ROOT = '/home/pierangelo/Scrivania/sagitairbox/sagitair'

STATIC_URL = '/static/'

MEDIA_ROOT = '/home/pierangelo/Scrivania/sagitairbox/sagitair/media/'

MEDIA_URL = "http://127.0.0.1:8000/media/"

MYDIR = "http://127.0.0.1:8000"

#TEMPLATE_DIRS = "/home/pierangelo/Scrivania/sagitairbox/sagitair/sito/templates/"


#Adjust the thumbnail processors for easy-thumbnails
from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS
 
from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

###
IMAGE_CROPPING_THUMB_SIZE = (1425, 500)
#cropping = ImageRatioField('image', '1425x500', size_warning=True)
IMAGE_CROPPING_SIZE_WARNING = True