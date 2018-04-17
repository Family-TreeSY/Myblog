# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Link, SideBar


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "href",
        "weight",
        "author",
        "created_time",
    ]
    fields = (
        ("title", "weight"),
        "href",
        "author",
    )


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "status",
        "display_type",
        "author",
        "created_time",
    ]
    fields = (
        ("title", "status"),
        "display_type",
        "author",
        "content",
    )
