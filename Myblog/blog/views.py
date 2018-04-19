# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment


class BasePostView(ListView):
    """
    IndexView,CategoryView,TagView都是指向文章post的，所以这里写一个父类BasePostView
    """
    model = Post
    template_name = "blog/list.html"
    context_object_name = "posts"


class IndexView(BasePostView):
    pass


class CategoryView(BasePostView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        # self.kwargs:获取url中的名字,(?P<category_id>\d+)
        cate_id = self.kwargs.get("category_id")
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostView):
    def get_queryset(self):
        tag_id = self.kwargs.get("tag_id")
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []
        posts = tag.posts.all()
        return posts


class PostView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"


def get_common_context():
    """分类
        1、nav_cates = categoryies.filter(is_nav=True) 导航分类
        2、cates = categories.filter(is_nav=False) 普通分类
        3、Category.objects.all()返回一个queryset对象复制给categories
        """
    categories = Category.objects.all()
    cates = []
    nav_cates = []
    for category in categories:
        if category.is_nav:
            nav_cates.append(category)
        else:
            cates.append(category)

    """
    侧边栏
    """
    sidebars = SideBar.objects.filter(status=1)
    recently_posts = Post.objects.filter(status=1)[:5]
    recently_comments = Comment.objects.filter(status=1)[:2]
    context = {
        "nav_cates": nav_cates,
        "cates": cates,
        "sidebars": sidebars,
        "recently_posts": recently_posts,
        "recently_comments": recently_comments,
    }
    return context
