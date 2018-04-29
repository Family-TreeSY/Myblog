# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dal import autocomplete

from blog.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    """
    重写get_queryset方法
    request.user表示当前用户
    判断当前用户是否登陆，如果没有就不返回任何查询集

    获取所有分类，如果有这个分类就过滤出以这个分类开头的所有数据不区分大小写
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Category.objects.none()

        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        qs = Tag.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
