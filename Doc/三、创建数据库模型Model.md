---
title: 创建数据库模型Model
date: 2018-4-2 22:08:08
tags:
- Django
---
### 三、创建数据库模型Model
- blog 
- config
- comment

**blog**
> author、category都有外键（foreignkey一对多关系），每篇文章只有一个分类，而一个分类下可以有多篇文章
> 
> tag的ManyToManyField字段是多对多关系，一篇文章可以有多个标签，一个标签下也可以有多篇文章


```python
# blog/models.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    STATUS_ITEMS = (
        (1, "正常"),
        (2, "删除"),
    )
    name = models.CharField(max_length=50, verbose_name="名城")
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name="状态"
    )
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, "正常"),
        (2, "删除"),
    )
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name="状态"
    )
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "标签"


class Post(models.Model):
    """
    1、指定title字段类型为字符（charfield）
    2、max_length指定字符长度
    3、verbose_name可以理解为注释
    4、Textfild因为是正文内容，输入会非常长
    5、status默认为1,意思是文章默认状态是上线状态
    6、auto_now_add为创建时使用
    7、auto_now为更新时使用
    """
    STATUS_ITEM = (
        (1, "上线"),
        (2, "删除"),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文内容", help_text="正文必须为markdown")
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEM, verbose_name="状态"
    )
    category = models.ForeignKey(Category, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = verbose_name_plural = "文章"
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    STATUS_ITEMS = (
        (1, "正常"),
        (2, "删除"),
    )
    name = models.CharField(max_length=50, verbose_name="名城")
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name="状态"
    )
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, "正常"),
        (2, "删除"),
    )
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name="状态"
    )
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "标签"


class Post(models.Model):
    """
    1、指定title字段类型为字符（charfield）
    2、max_length指定字符长度
    3、verbose_name可以理解为注释
    4、Textfild因为是正文内容，输入会非常长
    5、status默认为1,意思是文章默认状态是上线状态
    6、auto_now_add为创建时使用
    7、auto_now为更新时使用
    """
    STATUS_ITEM = (
        (1, "上线"),
        (2, "删除"),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文内容", help_text="正文必须为markdown")
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEM, verbose_name="状态"
    )
    category = models.ForeignKey(Category, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = verbose_name_plural = "文章"

```


**config**
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    """友链"""
    STATUS_ITEMS = (
        (1, "正常"),
        (2, "删除"),
    )
    title = models.CharField(max_length=50, verbose_name="名称")
    href = models.URLField(verbose_name="链接")
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name="状态"
    )
    weight = models.PositiveIntegerField(
        default=1, choices=zip(
            range(1, 6), range(1, 6),
        ), verbose_name="权重", help_text="权重越高展示顺序越靠前"
    )
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "友链"


class SideBar(models.Model):
    """侧边栏"""
    STATUS_ITEMS = (
        (1, "展示"),
        (2, "下线")
    )
    SIDE_TYPE = (
        (1, "HTML"),
        (2, "最新文章"),
        (3, "最热文章"),
        (4, "最热评论"),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name="状态"
    )
    display_type = models.PositiveIntegerField(
        default=1, choices=SIDE_TYPE, verbose_name="展示类型"
    )
    content = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="内容",
        help_text="如果设置的不是HTML类型，可为空"
    )
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"

```

**comment**
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    target = models.CharField(max_length=200, null=True, verbose_name='评论目标')
    content = models.CharField(max_length=2000, verbose_name='内容')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name='状态'
    )
    website = models.URLField(verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'


```

[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)