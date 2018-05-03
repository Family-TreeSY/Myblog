---
title: 增加PV、UV模块
date: 2018-4-8 18:08:08
tags:
- Django
---
### **二十一、增加PV、UV模块**

- Page-View(pv)：即页面浏览量，通常是衡量一个网络新闻频道或网站甚至一条网络新闻的主要指标
- Unique Visitor(uv)：是指通过互联网访问、浏览这个网页的自然人

这一小节来总结下pv、uv的植入，**先创建模型加入admin在后台展示，因为修改了模型别忘了迁移数据库**

- 引入cache



```python
# blog/models.py


 pv = models.PositiveIntegerField(default=0, verbose_name="pv")
 uv = models.PositiveIntegerField(default=0, verbose_name="uv")
```

编辑视图函数，这是最简单的pv、uv实现，但它有很大的问题，假如有100个人同时点击这篇文章，pv显示还是一次，uv的话需要设置为同一个用户在24小时内点击同一篇文章只显示一次，现在只要刷新页面就是一次pv和uv的增加

```python
# blog/views.py


 def get(self, request, *args, **kwargs):
        response = super(PostView, self).get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        self.object.pv = self.object.pv + 1
        self.object.uv = self.object.uv + 1
        self.object.save()

```

这里，我们发现在视图层面处理数据层面的代码并不合理，视图层负责逻辑处理，所以改一下代码

```python
# blog/models.py
from django.db.models import F

  def increase_pv(self):
        """
        F()允许Django在未实际链接数据的情况下具有对数据库字段的值的引用，
        不用获取对象放在内存中再对字段进行操作，直接执行原生产sql语句操作
        """
        return type(self).objects.filter(id=self.id).update(pv=F('pv') + 1)

    def increase_uv(self):
        return type(self).objects.filter(id=self.id).update(uv=F('uv') + 1)

```


```python
# blog/views.py


    def get(self, request, *args, **kwargs):
        response = super(PostView, self).get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        self.object.increase_pv()
        self.object.increase_uv()
```

到这里pv已经没有问题了，uv需要用Django的cache来控制它的访问量

我们先把pv、uv显示到前台去，文章列表页只显示pv

```python
# template/blog/list.html


<nav class="nav">
                  分类:<a class="nav-link post-element-nav" href="{% url 'category' post.category_id %}">{{ post.category }}</a>
                  {% for tg in post.tag.all %}
                  标签:<a class="nav-link post-element-nav" href="{% url 'tag' tg.id %}">
                  {{ tg.name }}
                  {% endfor %}</a>
                  作者:<a class="nav-link post-element-nav" href="{% url 'author' post.author_id %}">{{ post.author }}</a>
                  创建时间:<a class="nav-link post-element-nav" href="#">{{ post.created_time }}</a>
                  阅读量:<a class="nav-link post-element-nav" href="#">{{ post.pv }}</a>
              </nav>
```

文章正文页显示pv和uv
```python
# template/blog/detail.html

 <nav class="nav">
      分类:<a class="nav-link post-element-nav" href="{% url 'category' post.category_id %}">{{ post.category }}</a>
      {% for tg in post.tag.all %}
      标签:<a class="nav-link post-element-nav" href="{% url 'tag' tg.id %}">
      {{ tg.name }}
      {% endfor %}</a>
      作者:<a class="nav-link post-element-nav" href="#">{{ post.author }}</a>
      创建时间:<a class="nav-link post-element-nav" href="#">{{ post.created_time }}</a>
      阅读量:<a class="nav-link post-element-nav" href="#">{{ post.pv }} | {{ post.uv }}</a>
  </nav>

```

效果如下
![列表页](http://m.qpic.cn/psb?/V10WDaE22S84Sl/N.gJ0iTFp1sZLEcuiWbQVjARRDsUiiWlpJJYbiSOFuQ!/b/dJUAAAAAAAAA&bo=PwQvAgAAAAADBzQ!&rf=viewer_4)

![正文页](http://m.qpic.cn/psb?/V10WDaE22S84Sl/eevNGK75MA.0RQmuBA*JzIafRo0gM3Hn6qhxbMR8V68!/b/dDIBAAAAAAAA&bo=wwOZAgAAAAADF2k!&rf=viewer_4)


在侧边栏新增最热文章，根据pv的数量来排列

```python
# base.html

{% elif side.display_type == 3 %}
<ul>
     {% for post in hot_posts %}
     <li><a href="{% url 'detail' post.pk %}">{{ post.title }} - {{ post.pv }}</a></li>
     {% endfor %}
 </ul>

```

```python
# blog/views.py


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

```

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/BWJU7DSV0QGZSTeXPwiuUkReQvKOw1HOwQmg0ph9acg!/b/dDEBAAAAAAAA&bo=MwZCAgAAAAADB1c!&rf=viewer_4)


**引入cache**

引入cache来控制uv，同一个用户在24小时内访问同一篇文章就+1，pv这里也重新设置下，同一用户在30秒内访问多次，pv只+1

- 首先先获取cookie
- pv_key的值是用户和文章获取路径
- 后面if逻辑的意思是：pv如果用户在30秒内没有访问过，那么就+1
- uv也一样，只不过它的时间限制更长，uv如果用户在24小时内没有访问过，那么就+1


```python
# blog/views.py


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
            cache.set(uv_key, 1, 60*60*24)

```


[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)