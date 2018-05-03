---
title: Django-Silk
date: 2018-4-8 22:08:08
tags:
- Django
- Silk
---
### **二十七、配置Django-Silk**

Silk是一个Django框架的分析检查工具，功能主要包括： 

- 通过中间件拦截请求/响应 

- 围绕SQL执行情况进行数据库的查询和分析 

- 通过Python装饰器进行手动、动态地分析代码块和函数。

- 提供上述检测手段的可视化用户界面


同样，先安装模块

> pip install django-silk


在settings/develop.py中配置如下


```python
# develop.py



INSTALLED_APPS += [
    'debug_toolbar',
    'silk',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware',
]


```


配置urls.py



```python
# urls.py





urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
```


![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/XsUeq*nrHZBNMyEluaisWmEjcZPSES7TwJaPN.aWC0k!/b/dEEBAAAAAAAA&bo=TgdGAgAAAAADBy8!&rf=viewer_4)






[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)

