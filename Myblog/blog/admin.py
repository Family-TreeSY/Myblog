# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from Myblog.custom_site import custom_site
from Myblog.custom_admin import BaseOwnerAdmin


@admin.register(Post, site=custom_site)
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

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse("cus_admin:blog_post_change", args=(obj.id,))
        )
    # 不加简短描述，管理界面会显示operator
    operator.short_description = "操作"

    # 保证每条数据都属于当前用户
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = [
        "name",
        "status",
        "is_nav",
        "author",
        "created_time",
        "operator",
    ]
    fields = (
        "name",
        "status",
        "is_nav",
        "author",
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse("cus_admin:blog_category_change", args=(obj.id,))
        )
    # 不加简短描述，管理界面会显示operator
    operator.short_description = "操作"


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = [
        "name",
        "status",
        "author",
        "created_time",
        "operator",
    ]
    fields = (
        "name",
        "status",
        "author",
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse("cus_admin:blog_tag_change", args=(obj.id,))
        )
    # 不加简短描述，管理界面会显示operator
    operator.short_description = "操作"
