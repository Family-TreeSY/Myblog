---
title: admin替换为xadmin
date: 2018-4-8 19:08:08
tags:
- Django
---
### **二十二、admin替换为xadmin**
Django自带的后台管理有点简陋，这一节把admin管理后台替换为xadmin

[xadminGitHub](https://github.com/sshwsfc/xadmin)

安装xadmin建议使用git安装，直接pip install xadmin会少包，后面补上，运行时也是各种报错

> pip install xadmin git+https://github.com/sshwsfc/xadmin.git


**第一步**
**把三个app中的admin.py全部改为adminx.py**，这里就操作blog/adminx.py作为示例，Row()：把括号内的字段放在一行

```python
blog/adminx.py


import xadmin
from xadmin.layout import Row, Fieldset

from Myblog.adminx import BaseOwnerAdmin


# @admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    """
    1、list_display是展示页面的内容
    2、search_fileds：搜索框
    3、list_filter：页面右侧的过滤栏，以作者来过滤
    4、date_hierarchy:创建时间
    5、fields：编辑页面所要展示的字段
    """
    form = PostAdminForm
    list_display = [
        "title",
        "status",
        "category",
        "author",
        "pv",
        "uv",
        "created_time",
        "operator",
    ]
    search_fields = [
        "title",
        "category__name",
        "author__username",
    ]
    list_filter = (
        "category",
        "author",
    )
    date_hierarchy = "created_time"
    # 编辑页面
    # fields = (
    #     ("title", 'category'),
    #     "tag",
    #     "author",
    #     "desc",
    #     "status",
    #     "content",
    #     "is_markdown",
    #     "html",
    # )
    form_layout = (
        Fieldset(
            "基础信息",
            'title',
            'desc',
            'author',
            Row('category', 'tag', 'status'),
            Row('content', 'is_markdown'),
        ),
    )
    # 编辑页面不包含以下字段
    exclude = (
        "html",
        "pv",
        "uv",
    )
xadmin.site.register(Post, PostAdmin)

```

**第二步**
原先的站点也不需要了，删掉custom_site.py，把cus_admin.py改名为adminx.py，BaseOwnerAdmin原先继承的admin也不需要了，直接object，新建一个GlobalSetting类给xadmin后台更改标题名字


```python
# Myblog/adminx.py


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from xadmin.views import CommAdminView

class BaseOwnerAdmin(object):
        def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin, self).get_list_queryset()
        # 是超级用户返回qs
        if request.user.is_superuser:
            return qs
        # 不是返回自己用户
        return qs.filter(owner=request.user)

    def save_models(self):
        # import pdb;pdb.set_trace()
        if not self.org_obj:
            self.new_obj.author = self.request.user
        return super(BaseOwnerAdmin, self).save_models()


class GlobalSetting(CommAdminView):
    """后台设置"""
    site_title = 'Myblog'
    site_footer = 'power by MyBlog@treehl'


xadmin.site.register(CommAdminView, GlobalSetting)


```



**第三步**

把xadmin注册到settings中的INSTALLED_APP

```python
# settings/base.py


INSTALLED_APPS = [
  
    'xadmin',
    'crispy_forms',
    'reversion',


```


最后设置url

```python
# urls.py


import xadmin
from xadmin.plugins import xversion


xadmin.autodiscover()
xversion.register_models()




urlpatterns = [
	...................
    url(r'^admin/', xadmin.site.urls),
]


```

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/8JzBxIa8LUdvOFbs2IBthWgBLdEmHG9d1h4lhGKxhHg!/b/dDIBAAAAAAAA&bo=VAdpAwAAAAADBxs!&rf=viewer_4)


[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)