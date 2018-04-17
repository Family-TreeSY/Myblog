# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment


@admin.register(Comment)
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
