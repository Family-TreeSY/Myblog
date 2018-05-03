---
title: 配置Cache Redis
date: 2018-4-8 23:10:08
tags:
- Django
- Redis
- Cache
---
### **二十九、配置Cache Redis**

这里配置redis来作为缓存，这里贴几个有关缓存的介绍
[什么是缓存](https://zhuanlan.zhihu.com/p/28200451)
[HTTP缓存](https://zhuanlan.zhihu.com/p/28200451)

django中提供的缓存方案大致有三种
- 全页面缓存
- 局部缓存（函数缓存）
- 函数中某块数据的缓存



首先配置cache
```python
# develop.py product.py


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "REDIS_CLIENT_CLASS": "fakeredis.FakeStrictRedis",
            }
        }
    }

```


接下来配置url，设置6分钟的缓存


```python
# urls.py


from django.views.decorators.cache import cache_page



.............

 url(r'^category/(?P<category_id>\d+)/$',
        cache_page(60*10)(CategoryView.as_view(), name="category")),

.............

```


在view层编写一个缓存装饰器


```python
# blog/views.py



def cache_it(func):
    def wrapper(self, *args, **kwargs):
        key = repr((func.__name__, args, kwargs))
        result = cache.get(key)
        if result:
            print("Hit cache!")
            return result
        print("Hit db")
        result = func(self, *args, **kwargs)
        cache.set(key, result, 60*5)
        return result
    return wrapper


class CommonMixin(object):
    @cache_it
    def get_category_context(self):
............................


```







[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)
