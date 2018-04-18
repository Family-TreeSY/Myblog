# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage

from .models import Post, Tag


def post_list(request, category_id=None, tag_id=None):
    """render()方法根据我们传入的参数来构造Httpresponse
        1、render传入Http请求后，根据第二个参数blog/list.html找到这个模板并且读取它的值
        2、context是字典数据，传递到模板
    """
    # 从第一页开始
    page = request.GET.get("page", 1)
    # 每页数据量
    page_size = 4
    try:
        page = int(page)
    except TypeError:
        page = 1

    queryset = Post.objects.all()
    if category_id:
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()

    # 创建Paginator实例,每页展示4篇文章
    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        # 页面超过页数范围就传递最后一页数据
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
    }
    return render(request, "blog/list.html", context=context)


def post_detail(request, pk=None):
    """pk就是post_id
    name的值会被传到模板中
    """
    try:
        queryset = Post.objects.get(pk=pk)
    except queryset.DoesNotExist:
        return Http404("Post is not exist!")
    context = {
        "post": queryset,
    }
    return render(request, "blog/detail.html", context=context)
