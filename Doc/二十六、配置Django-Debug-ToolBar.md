---
title: Django-Debug-Toolbar
date: 2018-4-8 21:08:08
tags:
- Django
- Debug-Toolbar
---
### **二十六、配置Django-Debug-ToolBar**


Debug-Toolbar可以优化性能，测量程序运行的时间是否是在预定范围内，查看访问速度，查询数据库操作，它只能在测试环境使用，所以不能注册到base.py中的INSTALLED_APP


首先安装

> pip install django-debug-toolbar


在develop环境中加载它


```python
# develop.py



INSTALLED_APPS += [
    'debug_toolbar',
    'silk',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# 只有在这个地址下才会生效
INTERNAL_IPS = ['127.0.0.1']

我可以看到bedug-toolbar前台并没有显示出来，因为它用的是google的jquery，这里需要配置cdn
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
}

```


![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/gELlTwezkp5Z78OUFqC1NGHTbcS2Hc0.j7wzGGqAc0E!/b/dDABAAAAAAAA&bo=bAehAgAAAAADB.o!&rf=viewer_4)




[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)

