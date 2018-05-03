---
title: 配置MySQL
date: 2018-4-8 23:08:08
tags:
- Django
- MySQL
---
### **二十八、配置MySQL**

- 配置MySQL
- 加载静态资源

**一、配置MySQL**
mysql数据库是准备用在上线阶段的，所以我们先创建生产环境，在settings目录中创建product.py

NOQA意思是告诉pep8检测工具，跳过这个

```python
# settings/product.py


# -*- coding:utf-8 -*-
from .base import * # NOQA


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog_db',
        'USER': 'root',
        'PASSWORD': '', # 这里写入自己的密码
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

```


然后，修改manage.py中的profile


```python
# manage.py


if __name__ == "__main__":
    profile = os.environ.get('MYBLOG_PROFILE', 'product')
    ...................

```

运行下服务，会提示需要安装mysqlclient，和迁移数据库

> pip install mysql-client



> python manage.py migrate



接下来进入mysql创建myblog_db数据库


> mysql -u root -p 


> create database mysql_db character set utf8mb4;
Query OK, 1 row affected (0.01 sec)


因为数据库改为mysql，原先数据都没有了，这里需要重新创建一个超级用户


> python manage.py createsuperuser

创建完成后进入后台管理，我们发现插件都不能使用，前端页面的css也wu'f



**二、加载静态资源**
之前抽取静态资源的时候，配置了static_root路径，现在可以排上用场了，在上级目录新建一个statuc_files目录

```python
# base.py


STATIC_ROOT = '../static_files/'


```



配置url



```python
# urls.py

import re
from django.views.static import serve

..................
def static(prefix, **kwargs):
    return [
        url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), serve, kwargs=kwargs),
    ]



urlpatterns = [
  ..................
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


```


最后运行python manage.py collectstatic  来收集静态资源，收集完成后在服务，

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/SuoMB*RuYHgJpPggEnPBV9s2U43fhI6NRXSxXvsAolc!/b/dDIBAAAAAAAA&bo=TwfiAgAAAAADB4o!&rf=viewer_4)



![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/ZvWfQ2ZyxFMYkOjCXDHAg0*UfhWgZtnh4bkFV2QL77E!/b/dGgBAAAAAAAA&bo=ZAdKAwAAAAADFxg!&rf=viewer_4)






[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)



