---
title: 函数视图
date: 2018-4-3 10:08:08
tags:
- Django
---

### **七、函数视图**
前面我们开完了后台管理，现在需要开发前台将后台数据展示出来，这里先使用函数视图来开发

**一、博客所需要的页面**
- 首页（列表页）
- 文章正文页
- 标签页
- 分类页

不同的页面需要不同的url，所以先配置下urls.py

```python
from django.conf.urls import url
from django.contrib import admin

from .custom_site import custom_site
from blog.views import post_list, post_detail

urlpatterns = [
    url(r'^$', post_list),
    url(r'^category/(?P<category_id>\d+)/$', post_list),
    url(r'^tag/(?P<tag_id>\d+)/$', post_list),
    url(r'^post/(?P<post_id>\d+)/$', post_detail),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
```

urls.py配置完成后，就需要编写view试图
```python
# blog/views.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def post_list(request):
    return HttpResponse("Hello, World!")

def post_detail(request, pk=None):
    return HttpResponse("Hello, World!")

```

运行服务查看下，页面出现了Hello,World
![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/auYvoZQn5lMfMlhv7Tlo2VLslPaj8hoKJGT31NBev68!/b/dDABAAAAAAAA&bo=Wgd.AAAAAAADBwE!&rf=viewer_4)


**二、正开发**
先在Myblog下创建templates文件夹，在templates内创建list.html和detail.html，不要忘记加上__init__.py

│  custom_admin.py
│  custom_admin.pyc
│  custom_site.py
│  custom_site.pyc
│  db.sqlite3
│  urls.py
│  urls.pyc
│  wsgi.py
│  wsgi.pyc
│  __init__.py
│  __init__.pyc
│
├─settings
│      base.py
│      base.pyc
│      develop.py
│      develop.pyc
│      __init__.py
│      __init__.pyc
│
└─templates
        detail.html
        list.html
        __init__.py



编辑blog/views.py
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def post_list(request, category_id=None, tag_id=None):
    """render()方法根据我们传入的参数来构造Httpresponse
        1、render传入Http请求后，根据第二个参数blog/list.html找到这个模板并且读取它的值
        2、context是字典数据，传递到模板
    """
    context = {
        "post_list": post_list,
    }
    return render(request, "blog/list.html", context=context)


def post_detail(request, pk=None):
    """pk就是post_id
    name的值会被传到模板中
    """
    context = {
        "name": "Treehl",
    }
    return render(request, "blog/detail.html", context=context)
```

接下来编辑list.html，detail.html，这个可以自由发挥，**不要忘记把Myblog添加到INSTALLED_APPS**

```python
# list.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Treehl的博客</title>
</head>
<body>
<h1>Hello, World</h1>
<p>Learing Django</p>
</body>
</html>

```

```python
# detail.html

<html>
<body>
<a href="https://docs.djangoproject.com/en/2.0/topics/http/urls/">HTML</a>
<p>post content</p>
</body>
</html>

```

可以开启服务查看下
- http://127.0.0.1:8000/post/1/
- http://127.0.0.1:8000/category/1/
- http://127.0.0.1:8000/tag/1/
- http://127.0.0.1:8000/
![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/8G9zwzNpnZgwSu4QnJc65iV2sF2Qkbh1KeXPIX.z*gM!/b/dGcBAAAAAAAA&bo=dwefAAAAAAADB80!&rf=viewer_4)


接下来需要将文章、分类、标签体现在页面上，重写views.py
- Post.objects.all()返回所有文章，也可以这样理解，它返回一个queryset对象，并且赋值给queryset变量，objects就是一个数据接口，queryset是懒加载的，queryset = Post.objects.all()并没有调出数据

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404

from .models import Post, Tag


def post_list(request, category_id=None, tag_id=None):
    """render()方法根据我们传入的参数来构造Httpresponse
        1、render传入Http请求后，根据第二个参数blog/list.html找到这个模板并且读取它的值
        2、context是字典数据，传递到模板
    """
    queryset = Post.objects.all()
    if category_id:
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()
    context = {
        "posts": queryset,
    }
    return render(request, "blog/list.html", context=context)


def post_detail(request, pk=None):
    """pk就是post_id
    name的值会被传到模板中
    """
    try:
        queryset = Post.objects.get(pk=pk)
    except queryset.DoesNotExist:
        return Http404("Post is not exist!")
    context = {
        "post": queryset,
    }
    return render(request, "blog/detail.html", context=context)

```

接下来，我们需要给blog/models.py中的Tag类增加反向查询
> tag = models.ManyToManyField(Tag, related_name= "posts", verbose_name="标签")


编辑list.html  ，这里用到了模板标签{% for %}将文章遍历出来，再使用模板变量{{ }}将数据体现在页面
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Treehl的博客</title>
</head>
<body>
<h1>Treehl的博客</h1>
<ul>
    {% for post in posts %}
    title: {{ post.title }}<br/>
    desc: {{ post.desc }}
    <hr/>
    {% endfor %}
</ul>
</body>
</html>

```

detail.html

```python

<html>
<body>
<a href="/">首页</a>
<h4>{{ post.title }}</h4>
{{ post.content }}
</body>
</html>

```

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/u1aGEhuHwdCSBFW4gIar9YcMh*ec09wNXSVN1aQ0I50!/b/dEEBAAAAAAAA&bo=JgcsAgAAAAADBy0!&rf=viewer_4)

接下来，我们需要在列表页创建文章链接（可以进入正文页），我们为了不把代码写死，可以在url中添加 name= "..."
```python
urlpatterns = [
    url(r'^$', post_list, name="index"),
    url(r'^category/(?P<category_id>\d+)/$', post_list, name="category"),
    url(r'^tag/(?P<tag_id>\d+)/$', post_list, name="tag"),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name="detail"),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
]
```

编写list.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Treehl的博客</title>
</head>
<body>
<h1>Treehl的博客</h1>
<ul>
    {% for post in posts %}
    title: <a href="{% url 'detail' post.id %}">{{ post.title }}</a>><br/>
    desc: {{ post.desc }}
    <hr/>
    {% endfor %}
</ul>
</body>
</html>

```






[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)
