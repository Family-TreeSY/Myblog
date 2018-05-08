# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.html import format_html
from django.urls import reverse

import xadmin
from xadmin.layout import Fieldset, Row

from .models import Link, SideBar
from Myblog.adminx import BaseOwnerAdmin
from adminforms import SideBarAdminForm


# @admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = [
        "title",
        "href",
        "weight",
        "author",
        "created_time",
        "operator",
    ]
    form_layout = (
        Fieldset(
            "基础信息",
            'title',
            'weight',
            'href'
        ),
    )

    exclude = (
        'author',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse("cus_admin:config_link_change", args=(obj.id,))
        )
        # 不加简短描述，管理界面会显示operator

    operator.short_description = "操作"


xadmin.site.register(Link, LinkAdmin)


# @admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    form = SideBarAdminForm
    list_display = [
        "title",
        "status",
        "display_type",
        "created_time",
        "operator"
    ]

    form_layout = (
        Fieldset(
            "基础信息",
            Row('title', 'status'),
            'display_type',
            'content',
        ),
    )

    exclude = (
        'author',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse("cus_admin:config_sidebar_change", args=(obj.id,))
        )
        # 不加简短描述，管理界面会显示operator

    operator.short_description = "操作"


xadmin.site.register(SideBar, SideBarAdmin)
