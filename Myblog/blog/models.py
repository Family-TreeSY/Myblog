# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


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

    def __unicode__(self):
        return self.title
