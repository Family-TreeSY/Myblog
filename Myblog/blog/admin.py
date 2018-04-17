# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    1、list_display是展示页面的内容
    2、search_fileds：搜索框
    3、list_filter：页面右侧的过滤栏，以作者来过滤
    4、date_hierarchy:创建时间
    5、fields：编辑页面所要展示的字段
    """
    list_display = [
        "title",
        "status",
        "category",
        "author",
        "created_time",
    ]
    search_fields = [
        "title",
        "category__name",
        "author__username",
    ]
    list_filter = (
        "author",
        "status",
    )
    date_hierarchy = "created_time"
    # 编辑页面
    fields = (
        ("title", 'category'),
        "tag",
        "author",
        "desc",
        "status",
        "content",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "status",
        "is_nav",
        "author",
        "created_time",
    ]
    fields = (
        "name",
        "status",
        "is_nav",
        "author",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "status",
        "author",
        "created_time",
    ]
    fields = (
        "name",
        "status",
        "author",
    )
