# -*- coding:utf-8 -*-
from .base import * # NOQA


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog_db',
        'USER': 'root',
        'PASSWORD': 'root', # 这里写入自己的密码
        'HOST': '127.0.0.1',
        'PORT': 3306,
        # 'OPTIONS': {'charset': 'utf8mb4'}
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
    }
}

