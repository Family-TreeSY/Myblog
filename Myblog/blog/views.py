# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.core.cache import cache

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment
from comment.views import CommonShowMixin


def cache_it(func):
    def wrapper(self, *args, **kwargs):
        key = repr((func.__name__, args, kwargs))
        result = cache.get(key)
        if result:
            print("Hit cache!")
            return result
        print("Hit db")
        result = func(self, *args, **kwargs)
        cache.set(key, result, 60 * 5)
        return result
    return wrapper


class CommonMixin(object):
    # @cache_it
    def get_category_context(self):
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
        return {
            "nav_cates": nav_cates,
            "cates": cates,
        }

    def get_context_data(self, **kwargs):
        """
        侧边栏
        """
        sidebars = SideBar.objects.filter(status=1)
        recently_posts = Post.objects.filter(status=1)[:5]
        recently_comments = Comment.objects.filter(status=1)[:2]
        hot_posts = Post.objects.filter(status=1).order_by("-pv")[:5]
        kwargs.update({
            "sidebars": sidebars,
            "recently_posts": recently_posts,
            "recently_comments": recently_comments,
            "hot_posts": hot_posts,
        })
        kwargs.update(self.get_category_context())
        return super(CommonMixin, self).get_context_data(**kwargs)


class BasePostView(CommonMixin, ListView):
    """
    IndexView,CategoryView,TagView都是指向文章post的，所以这里写一个父类BasePostView
    """
    model = Post
    paginate_by = 10
    template_name = "blog/list.html"
    context_object_name = "posts"


class IndexView(BasePostView):
    """增加搜索功能
    1、数据过滤
    2、数据传递到模板里
    3、request.GET.get(query):通过get请求获取的数据都存放在request.GET中，
    所以它是一个字典对象，用get来获取query键
    4、如果query存在就过滤出所有以query开头的数据，i表示不区分大小写，
    如果query不存在就返回
    """

    def get_queryset(self):
        query = self.request.GET.get("query")
        qs = super(IndexView, self).get_queryset()
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)


class CategoryView(BasePostView):
    """覆写get_queryset方法
    1、该方法默认获取指定模型的全部列表数据,为了获取指定分类下的文章列表数据，我们覆写该方法，改变它的默认行为
    2、self.kwargs从url中得到category_id
    3、get_queryset获取全部文章后再使用filter来过滤分类并返回
    """

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


class AuthorView(BasePostView):
    def get_queryset(self):
        query = self.kwargs.get("author_id")
        qs = super(AuthorView, self).get_queryset()
        if query:
            qs = qs.filter(author_id=query)
        return qs


class PostView(CommonMixin, CommonShowMixin, DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"

    def get(self, request, *args, **kwargs):
        response = super(PostView, self).get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        """pv、uv
        1、首先先获取cookie
        2、pv_key的值是用户和文章获取路径
        3、后面if逻辑的意思是：pv如果用户在30秒内没有访问过，那么就+1
        4、uv也一样，只不过它的时间限制更长，uv如果用户在24小时内没有访问过，那么就+1
        """
        sessionid = self.request.COOKIES.get("sessionid")
        if not sessionid:
            return

        pv_key = "pv:%s:%s" % (sessionid, self.request.path)
        if not cache.get(pv_key):
            self.object.increase_pv()
            cache.set(pv_key, 1, 30)

        uv_key = "uv:%s:%s" % (sessionid, self.request.path)
        if not cache.get(uv_key):
            self.object.increase_uv()
            cache.set(uv_key, 1, 60 * 60 * 24)
