# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment
from Myblog.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "target",
        "nickname",
        "status",
        "email",
        "created_time",
    ]
    fields = (
        ("target", "status"),
        "content",
        "website",
        "email",
    )
