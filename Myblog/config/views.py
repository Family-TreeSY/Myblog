# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from blog.views import CommonMixin
from .models import Link


class LinkView(CommonMixin, ListView):
    # 过滤出状态为正常的链接
    queryset = Link.objects.filter(status=1)
    model = Link
    template_name = "config/link.html"
    context_object_name = "links"
