# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def post_list(request, category_id=None, tag_id=None):
    """render()方法根据我们传入的参数来构造Httpresponse
        1、render传入Http请求后，根据第二个参数blog/list.html找到这个模板并且读取它的值
        2、context是字典数据，传递到模板
    """
    context = {
        "post_list": post_list,
    }
    return render(request, "blog/list.html", context=context)


def post_detail(request, pk=None):
    """pk就是post_id
    name的值会被传到模板中
    """
    context = {
        "name": "Treehl",
    }
    return render(request, "blog/detail.html", context=context)
