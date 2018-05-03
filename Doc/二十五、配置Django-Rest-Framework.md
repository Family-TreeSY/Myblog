---
title: Django-Rest-Framework
date: 2018-4-8 20:08:08
tags:
- Django
- Rest-Framework
---
### **二十五、配置Django-Rest-Framework**


- 配置Post、Category、Tag、User的API
- API doc文档
- 使分类和标签变为可读
- post分页
- 制定详情页
- 分类标签详情页做分页
- 修改创建时间

先安装 rest-framework

> pip install django-rest-framework



**一、配置Post、Category、Tag的API**
首先将rest-framework注册到INSTALLED_APP中

```python
# base.py

...........

'rest_framework',

```


接下来在blog/中新建api.py，这里就写了post、user的api，分类和标签的代码也一样

```python
# blog/api.py


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
             'url', 'title', 'pv', 'uv', 'author', 'category', 'tag', 'created_time'
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
             'id', 'username',
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer


```


再来配置url

```python
# urls.py


from rest_framework import routers
from blog.api import PostViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'user', UserViewSet)


url(r'^api/', include(router.urls)),



```

开启服务查看下
> http://localhost:8000/api/post/

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/lh5gJJ4TsaYoLA5leQGQENT..9gp0wbkF9eBq9PuRUI!/b/dDMBAAAAAAAA&bo=ZQYfAwAAAAADB10!&rf=viewer_4)



**二、配置API DOC **


> pip install coreapi


在urls.py中配置


```python
# urls.py


from rest_framework.documentation import include_docs_urls

..........................
url(r'^api/docs/', include_docs_urls(title="Myblog API")),

```


> http://localhost:8000/docs/#

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/n8WHOIAM.wTEvNeJpD2wdgShoS6HEcX*I5txgyyjaGE!/b/dDABAAAAAAAA&bo=fgfnAQAAAAADB70!&rf=viewer_4)



**三、使分类、标签、作者变为可读**


```python
# api.py



class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,  # api接口展示是中文
    )

    tag = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,  # api接口展示是中文
        many=True,  # 多对多
    )

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,  # api接口展示是中文
    )


```

效果如下


![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/gjll*7uqW7uBFBD3NCzDZn0pT.rJiki*iadVmAf0ksg!/b/dDIBAAAAAAAA&bo=FweNAgAAAAADB70!&rf=viewer_4)


**四、分页**

在settings/base.py中配置，文章列表页的分页，设置为每页数据为3
```python
# base.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 3
}
```


**五、制定详情页**
这里以tag为例，我们进入tag列表页后进入tag详情页发现和列表页一样，这里我们需要在tag详情页展示文章

```python
# api.py


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
             'url', 'name', 'status', 'author', 'created_time',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(
        many=True,
        read_only=True,
        )

    class Meta:
        model = Tag
        fields = (
            'id', 'name', 'posts'
        )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(status=1)
    serializer_class = TagSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TagDetailSerializer
        return super(TagViewSet, self).retrieve(request, *args, **kwargs)


```




**六、分类标签详情页做分页**


这里我们还可以给分类和标签做分页，这里有两种办法，第一种在postviewset下面新增get_queryset方法



```python

    def get_queryset(self):
        qs = super(PostViewSet, self).get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs
```

另外一种以tag示例

```python
from rest_framework import serializers, viewsets, pagination


class TagDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        posts = obj.posts.all()
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }


```

效果如下

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/hdFaDXixGwR*mba3zTGRfobEXYPoMyVaSjQLYGZCyQs!/b/dDMBAAAAAAAA&bo=jAaQAgAAAAADBzo!&rf=viewer_4)


![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/VSZXub.cxuSytEv3arQPT1.ai0oXHPa.3c4PKu4Q5zY!/b/dEQBAAAAAAAA&bo=6gZeAgAAAAADF4I!&rf=viewer_4)




** 七、修改创建时间**
修改PostSerializer类，DateTimeFiled下%Y-%m-%d %H:%M:%S，对应的分别是年、月、日
小时、分钟、秒
```python
# api.py

  created_time = serializers.DateTimeField(
        # year-month-date hour:minute:second
        format="%Y-%m-%d %H:%M:%S"
    )
```




[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)

