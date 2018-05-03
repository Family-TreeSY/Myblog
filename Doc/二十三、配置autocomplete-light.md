---
title: 配置autocomplete-light
date: 2018-4-8 19:08:08
tags:
- Django
- Autocomplete-light
---
### **二十三、配置autocomplete-light**

这里打开xadmin管理后台，我们发现页面会把所有的categroy和tag一起加载出来，假如有10000个分类必然会影响页面的加载速度，这里就要使用autocomplete-light来优化性能，配置它也很简单

> pip install django-autocomplete-light

先把autocomplete注册到INSTALLED_APP中

```python
# base.py



    'dal',
    'dal_select2',

```


在Myblog/下新建autocomplete.py，重写get_queryset方法，request.user表示当前用户，判断当前用户是否登陆，如果没有就不返回任何查询集，获取所有分类，如果有这个分类就过滤出以这个分类开头的所有数据不区分大小写

```python
# autocomplete.py


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dal import autocomplete

from blog.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Category.objects.none()

        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

```

最后，配置url


```python
# urls.py


from .autocomplete import CategoryAutocomplete, TagAutocomplete

 url(r'^category-autocomplete/$',
        CategoryAutocomplete.as_view(),
        name='category-autocomplete'),
    url(r'^tag-autocomplete/$',
        TagAutocomplete.as_view(),
        name='tag-autocomplete'),
     

```





[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)