# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

import markdown


class Category(models.Model):
    STATUS_ITEMS = (
        (1, "正常"),
        (2, "删除"),
    )
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name="状态"
    )
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


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

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    1、指定title字段类型为字符（charfield）
    2、max_length指定字符长度
    3、verbose_name可以理解为注释
    4、Textfild因为是正文内容，输入会非常长
    5、status默认为1,意思是文章默认状态是上线状态
    6、auto_now_add为创建时使用
    7、auto_now为更新时使用
    8、blank是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
    """
    STATUS_ITEM = (
        (1, "上线"),
        (2, "删除"),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    is_markdown = models.BooleanField(verbose_name="使用markdown", default=True)
    content = models.TextField(verbose_name="正文内容", help_text="注：正文可以使用markdown编辑")
    html = models.TextField(verbose_name='html渲染后的页面', default="", help_text='注：正文可以使用markdown编辑')
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEM, verbose_name="状态"
    )
    category = models.ForeignKey(Category, verbose_name="分类")
    tag = models.ManyToManyField(Tag, related_name="posts", verbose_name="标签")
    author = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    pv = models.PositiveIntegerField(default=0, verbose_name="pv")
    uv = models.PositiveIntegerField(default=0, verbose_name="uv")

    def save(self, *args, **kwargs):
        if self.is_markdown:
            self.html = markdown.markdown(
                self.content, extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                ]
            )
        else:
            self.html = self.content
        return super(Post, self).save(*args, **kwargs)

    def increase_pv(self):
        """
        F()允许Django在未实际链接数据的情况下具有对数据库字段的值的引用，
        不用获取对象放在内存中再对字段进行操作，直接执行原生产sql语句操作
        """
        return type(self).objects.filter(id=self.id).update(pv=F('pv') + 1)

    def increase_uv(self):
        return type(self).objects.filter(id=self.id).update(uv=F('uv') + 1)

    def status_show(self):
        return "当前状态:%s" % self.status
    status_show.short_description = "展示状态"

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        # 指定排序，最新文章最靠前
        ordering = ['-id']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
