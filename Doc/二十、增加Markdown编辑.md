---
title: 增加Markdown编辑
date: 2018-4-8 17:08:08
tags:
- Django
---
### **二十、增加Markdown编辑**

这一节，先把正文内容改成markdown编辑形式的，到后面我们会使用ckeditor富文本编辑，先安装markdown模块
> pip install markdown

我们需要给Post模型新增点数据，判断是否使用markdown，默认是使用，再增加渲染后的页面
blog/modles/class Post

```python
# blog/modles/class Post

is_markdown = models.BooleanField(verbose_name="使用markdown", default=True)
html = models.TextField(verbose_name='html渲染后的页面', default="", help_text='注：正文可以使用markdown编辑')
```

改修了模型后需要迁移数据库，**在admin中加入新增加的模型**

> python manage.py makemigrations

> python manage.py migrate


编辑blog/models.py/
```python
# blog/models.py

class Post(models.Model):
......................
	 def save(self, *args, **kwargs):
	        if self.is_markdown:
	            self.html = markdown.markdown(
	                self.content, extensions=[
	                    'markdown.extensions.extra',
	                    'markdown.extensions.codehilite',
	                    'markdown.extensions.toc',
	                ]
	            )
	        return super(Post, self).save(*args, **kwargs)

```

打开服务看下，应该会看到页面出现了html代码，这需要在detail.html中增加{{ post.html|safe }}

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/mJnYPD*NSFYL4TwXpd7sS73u5ezsDQh4hQTO6zcAvSg!/b/dDIBAAAAAAAA&bo=zgPvAAAAAAADBwA!&rf=viewer_4)

```python
# detail.html


<div class="post-element-content">
{{ post.html|safe }}
</div>

```

再看看效果
![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/eHh9dmL4cg1f6GqqDsMstNOLu2QfWzYJKqcIfQw17Mg!/b/dEIBAAAAAAAA&bo=NARpAgAAAAADB3k!&rf=viewer_4)


刚刚做出来的样式还没有代码高亮，首先我们先安装Pygments，它可以帮我们渲染css

> pip install Pygments


接下里就是引入样式，我选择的是github样式，在css目录下创建github.css，样式就不写出来了，有需要的可以查看github

> static/github.css

最后使用模板继承

```python
#base.html
............
  <link rel="stylesheet" href="{% static 'css/base.css' %}">
      {% block style %}

      {% endblock %}

.............
```


```python
# detail.html


{% block style %}
    <link rel="stylesheet" href="{% static 'css/github.css' %}">
{% endblock %}

```


效果如下：

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/LiSPlptXOh0TTo8BzaspDWJxFu2yzdJ.D8Kn3zZfXWA!/b/dDEBAAAAAAAA&bo=DASoAgAAAAADB4A!&rf=viewer_4)



[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)