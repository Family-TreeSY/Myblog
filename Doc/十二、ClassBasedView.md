---
title: ClassBasedView
date: 2018-4-6 13:08:08
tags:
- DJango
---
### **十二、ClassBasedView**

Class BasedView可以让我们的代码变的可扩展，减少视图函数的重复代码提升开发效率
- View： 用来处理简单的视图
- TemplateView：  继承自view，渲染模板
- ListView： 展示一个Model数据的view，比如文章列表
- DetailView：  展示一个Model内的多条数据

首先，我们需要更改url, as_view()意思是将类视图转换为函数视图，IndexView就是列表视图
PostView就是正文视图

```python
# urls.py
from blog.views import IndexView, CategoryView, TagView, PostView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name="category"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="detail"),
```

接下里重写views.py，IndexView,CategoryView,TagView都是指向文章post的，所以这里写一个父类BasePostView
- model = Post 告诉Django我们要获取的模型是post
- template_name：指定模板
- context_object_name：指定获取的模型列表数据保存的变量名，这个变量会被传递给模板，和函数试图中的context一样

```python
from django.views.generic import ListView, DetailView


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


class PostView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"

```


**设置分页**
CBV也内置了分页功能，非常简单
> https://docs.djangoproject.com/en/2.0/topics/class-based-views/mixins/

在父类BasePostView中添加如下代码，表示一页有三篇文章
```python
paginate_by = 3
```

再重写list.html


```python

 {% if page_obj.has_previous %}<a href="?page={{ page_obj.previous_page_number }}">上一页</a>
        {% endif %}
        Page {{ page_obj.number }} of {{ paginator.num_pages }}.
        {% if page_obj.has_next %}<a href="?page={{ page_obj.next_page_number }}">下一页</a>
        {% endif %}
```


好了，分页就结束了

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/FN6zkpRE67H0VuaB3F6iM6fHq4WsnvweaKOZzo.*0So!/b/dDIBAAAAAAAA&bo=gAXzAQAAAAADB1U!&rf=viewer_4)



**通用代码**
博客的列表页和正文页都是需要侧边栏和分类导航的，这里我们使用到了多重继承Mixin，把Mixin写入BasePostView和PostView，这里我们把分类挑了出来也可以把sidebar挑出来

```python
class CommonMixin(object):
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
        kwargs.update({
            "sidebars": sidebars,
            "recently_posts": recently_posts,
            "recently_comments": recently_comments,
        })
        kwargs.update(self.get_category_context())
        return super(CommonMixin, self).get_context_data(**kwargs)
```



```python
class BasePostView(CommonMixin, ListView):

..........


class PostView(CommonMixin, DetailView):

```



[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)

