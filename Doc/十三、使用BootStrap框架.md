---
title: 使用Bootstrap框架
date: 2018-4-7 13:08:08
tags:
- DJANGO
- BootStrap
---
### **十三、使用BootStrap框架**
官网地址
> https://getbootstrap.com/

我们先在myblog应用中创建一个frontend文件夹，同时创建list.html和detail.html作为列表页和正文页，这里先做个大概的样子，后面再套进项目里
- 首页以列表形式展现，头部是分类导航和博客名字，底部有普通分类和页脚
- 正文也也有分类导航的博客名字，底部有普通分类和页脚，文章标题上面做了个面包屑导航
- 侧边栏展示最新文章之类，可以自由发挥



```python
# list.html


<!doctype html>
<html lang="en">
  <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

      <!-- Bootstrap CSS -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

      <title>Hello, world!</title>
    </head>
<body>

 <div class="container">
    <h3>
      Myblog
      <small class="text-muted"> - 基于Django多人博客系统</small>
    </h3>
</div>

<div class="container">
  <nav class="nav">
    <a class="nav-link active" href="#">Active</a>
    <a class="nav-link" href="#">Link</a>
    <a class="nav-link" href="#">Link</a>
    <a class="nav-link disabled" href="#">Disabled</a>
  </nav>
</div>
 <hr/>

<div class="container">
  <div class="row">
    <div class="col-9">
       <div class="post-element">
            <div>
              <h3 style="border-bottom: 1px solid #ccc">标题标题</h3>
              <div>
                  <nav class="nav">
                      分类:<a class="nav-link active" href="#">Python</a>
                      标签:<a class="nav-link" href="#">Django</a>
                      作者:<a class="nav-link" href="#">Treehl</a>
                      创建时间:<a class="nav-link disabled" href="#">2018 03-03</a>
                  </nav>
              </div>
              <div>
                  <p>>这是摘要</p>
              </div>
          </div>
        </div>
      <div class="post-element">
            <div>
              <h3 style="border-bottom: 1px solid #ccc">标题标题</h3>
              <div>
                  <nav class="nav">
                      分类:<a class="nav-link active" href="#">Python</a>
                      标签:<a class="nav-link" href="#">Django</a>
                      作者:<a class="nav-link" href="#">Treehl</a>
                      创建时间:<a class="nav-link disabled" href="#">2018 03-03</a>
                  </nav>
              </div>
              <div>
                  <p>>这是摘要</p>
              </div>
          </div>
        </div>
      <div class="post-element">
            <div>
              <h3 style="border-bottom: 1px solid #ccc">标题标题</h3>
              <div>
                  <nav class="nav">
                      分类:<a class="nav-link active" href="#">Python</a>
                      标签:<a class="nav-link" href="#">Django</a>
                      作者:<a class="nav-link" href="#">Treehl</a>
                      创建时间:<a class="nav-link disabled" href="#">2018 03-03</a>
                  </nav>
              </div>
              <div>
                  <p>>这是摘要</p>
              </div>
          </div>
        </div>
      <div class="post-element">
            <div>
              <h3 style="border-bottom: 1px solid #ccc">标题标题</h3>
              <div>
                  <nav class="nav">
                      分类:<a class="nav-link active" href="#">Python</a>
                      标签:<a class="nav-link" href="#">Django</a>
                      作者:<a class="nav-link" href="#">Treehl</a>
                      创建时间:<a class="nav-link disabled" href="#">2018 03-03</a>
                  </nav>
              </div>
              <div>
                  <p>>这是摘要</p>
              </div>
          </div>
        </div>

    </div>
    <div class="col-3">
      <div>
        <h3 style="border-bottom: 1px solid #ccc">标题标题</h3>
          <div>
              <p>这里是公告</p>
          </div>
      </div>
    </div>
  </div>
</div>
<footer class="footer">
  <div class="container">
     <nav class="nav">
      <a class="nav-link active" href="#">Active</a>
      <a class="nav-link" href="#">Link</a>
      <a class="nav-link" href="#">Link</a>
      <a class="nav-link disabled" href="#">Disabled</a>
     </nav>
  </div>
  <div class="container">
    <span class="text-muted">Power by Myblog@treehl</span>
  </div>
</footer>
</body>
</html>

```


```python
# detail.html


<!doctype html>
<html lang="en">
  <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

      <!-- Bootstrap CSS -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

      <title>Hello, world!</title>
    </head>
<body>

 <div class="container">
    <h3>
      Myblog
      <small class="text-muted"> - 基于Django多人博客系统</small>
    </h3>
</div>

<div class="container">
  <nav class="nav">
    <a class="nav-link active" href="#">Active</a>
    <a class="nav-link" href="#">Link</a>
    <a class="nav-link" href="#">Link</a>
    <a class="nav-link disabled" href="#">Disabled</a>
  </nav>
</div>
 <hr/>

<div class="container">
  <div class="row">
    <div class="col-9">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item"><a href="#">Library</a></li>
            <li class="breadcrumb-item active" aria-current="page">Data</li>
          </ol>
        </nav>
       <div class="post-element">
            <div>
              <h3 style="border-bottom: 1px solid #ccc">标题标题</h3>
            </div>
           <div>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
               <p>这是正文</p>
           </div>
       </div>

    </div>
    <div class="col-3">
      <div>
        <h3 style="border-bottom: 1px solid #ccc">标题标题</h3>
          <div>
              <p>这里是公告</p>
          </div>
      </div>
    </div>
  </div>
</div>
<footer class="footer">
  <div class="container">
     <nav class="nav">
      <a class="nav-link active" href="#">Active</a>
      <a class="nav-link" href="#">Link</a>
      <a class="nav-link" href="#">Link</a>
      <a class="nav-link disabled" href="#">Disabled</a>
     </nav>
  </div>
  <div class="container">
    <span class="text-muted">Power by Myblog@treehl</span>
  </div>
</footer>
</body>
</html>

```


接下来，我们需要把刚刚写的前端样式套进项目里，在templates目录下新建themes目录再新建default目录
> /templates/themes/defaults/blog/

重写base.html、list.html、detail.html，由于笔者对html和css不是很熟悉所以需要花点时间来写
下面用到的Django语法在前面也提过，还有就是些css和html，正文页用到的面包屑导航是套用bootstrap的组件
- {{  }}模板变量
- {% %} 模板标签
- {% url "category" post.id %} 设置url


```python
# base.html
<!doctype html>
<html lang="en">
  <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

      <!-- Bootstrap CSS -->
      <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css">
      <style>
            /*分类、标签、创建时间对齐样式和颜色*/
          .post-element-nav {
                padding-top: 0;
                padding-bottom: 0;
                color: #428bca;

          }
          /*文章标题字体大小以及对齐*/
          .post-element-title {
                font-size: 25px;
                border-bottom: 1px solid #ccc;
          }
          /*文章标题颜色*/
          .post-element-title a{
                color:#333;
          }
          /*分类导航与文章列表之间的距离*/
          .main {
                margin-top: 5px;
          }
           /*正文页内容与标题之间距离*/
          .post-element-content {
                margin-top: 10px;
          }
          .main ul {
                padding-left: 0px;
          }
           /*博客标题页边距*/
          .banner {
                margin-top: 20px;
          }
           /*页脚距离普通分类的距离*/
          .power {
                margin-top: 20px;
          }
           /*侧边栏消除ul带来的点号*/
          .sidebar li {
                list-style: none;
          }
          .sidebar a {
                color: #444;
          }

      </style>

      <title>Treehl</title>
    </head>
<body>

<div class="container">
    <h3 class="banner">
      <a href="/">Treeh的博客</a>
      <small class="text-muted"></small>
    </h3>
</div>

<div class="container">
    <nav class="nav">
        <a class="nav-link" href="/">首页</a>
        {% for cate in nav_cates %}
        <a class="nav-link" href="{% url 'category' cate.id %}">{{ cate.name }}</a>
        {% endfor %}
    </nav>
</div>
<hr/>

<div class="container main">
    <div class="row">
        <div class="col-9">
            {% block content %}

            {% endblock %}
        </div>
        <div class="col-3">
            {% for sidebar in sidebars %}
                <div class="container sidebar">
                    <h4>{{ sidebar.title }}</h4>
                        <ul>
                            {% if sidebar.display_type == 1 %}
                            {% autoescape on %}
                                {{ sidebar.content }}
                            {% endautoescape %}
                            {% elif sidebar.display_type == 2 %}
                        </ul>
                        <ul>
                            {% for post in recently_posts %}
                                <li>
                                    <a href="{% url 'detail' post.id %}">{{ post.title }}</a>
                                </li>
                            {% endfor %}
                        </ul>
                        {% elif sidebar.display_type == 4%}
                        <ul>
                            {% for comment in recently_comments %}
                                <li>
                                    {{ comment.content }}
                                </li>
                            {% endfor %}
                        </ul>
                    {% endif %}
                </div>
            {% endfor %}
        </div>
    </div>

<hr/>
<div class="container">
 <nav class="nav">
     {% for cate in cates %}
     <a class="nav-link" href="{% url 'category' cate.id %}">{{ cate.name }}</a>
     {% endfor %}
 </nav>
</div>
<footer class="footer power">
  <div class="container">
    <span class="text-muted">Power by Myblog@treehl</span>
  </div>
</footer>
</div>
</body>
</html>
```


```python
# list.html


% extends "./base.html" %}

{% block content %}
<ul>
<div class="post-element">
  <div>
      {% if posts %}
        {% for post in posts %}
          <h3 class="post-element-title">
              <a href="{% url 'detail' post.id %}">{{ post.title }}</a>
          </h3>
          <div>
              <nav class="nav">
                  分类:<a class="nav-link post-element-nav" href="{% url 'category' post.category_id %}">{{ post.category }}</a>
                  {% for tg in post.tag.all %}
                  标签:<a class="nav-link post-element-nav" href="{% url 'tag' tg.id %}">
                  {{ tg.name }}
                  {% endfor %}</a>
                  作者:<a class="nav-link post-element-nav" href="#">{{ post.author }}</a>
                  创建时间:<a class="nav-link post-element-nav" href="#">{{ post.created_time }}</a>
              </nav>
          </div>
          <div>
              <p>> {{ post.desc }}</p>
          </div>
        {% endfor %}
          {% if page_obj.has_previous %}<a href="?page={{ page_obj.previous_page_number }}">上一页</a>
            {% endif %}
            Page {{ page_obj.number }} of {{ paginator.num_pages }}.
            {% if page_obj.has_next %}<a href="?page={{ page_obj.next_page_number }}">下一页</a>
            {% endif %}
      {% else %}
        Empty!
      {% endif %}
  </div>
</div>
</ul>
{% endblock %}


```


```python
# detail.html
{% extends "./base.html" %}

{% block content %}
<html>
<body>
<div>
     <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="/">首页</a></li>
        <li class="breadcrumb-item"><a href="{% url 'category' post.category_id %}">{{ post.category.name }}</a></li>
        <li class="breadcrumb-item active" aria-current="page">正文</li>
      </ol>
    </nav>
</div>

<h4>{{ post.title }}</h4>
<div>
  <nav class="nav">
      分类:<a class="nav-link post-element-nav" href="{% url 'category' post.category_id %}">{{ post.category }}</a>
      {% for tg in post.tag.all %}
      标签:<a class="nav-link post-element-nav" href="{% url 'tag' tg.id %}">
      {{ tg.name }}
      {% endfor %}</a>
      作者:<a class="nav-link post-element-nav" href="#">{{ post.author }}</a>
      创建时间:<a class="nav-link post-element-nav" href="#">{{ post.created_time }}</a>
  </nav>
</div>
<div class="post-element-content">
{{ post.content }}
</div>
</body>
</html>
{% endblock %}

```

还需要修改下试图中的模板路径

```python
# views.py
# 还有正文视图也需要修改

template_name = "themes/default/blog/list.html"


```

运行服务试试看吧，样式会有点简陋，但也确实学到了前端知识，在W3SCHOOL上学了html和css后的最佳实践，实在忍受不了"极简风格"的可以网上下载模板套进去就好
![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/Q5m.6DV0ZtIv6gtHMsSu7M9Y7FTEMSciVr.xnUON4SQ!/b/dFYBAAAAAAAA&bo=awcTAwAAAAADB14!&rf=viewer_4)


为了方便抽取静态文件，再次更改下模板路径

> themes/default/template/blog/...

在setting/base.py中增加路径

```python
THEME = 'themes/default'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, THEME, 'template')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

再次修改视图中的买平板渲染路径

```python

# views.py
template_name = "blog/list.html"
```


接下里，再次调整前端样式

```python
# base.html


<!doctype html>
<html lang="en">
  <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css">
      <style>
           <!--body {-->
                <!--background-color: #eeeeee; # 页面背景色-->
           <!--}-->
           .fixed-top {
                position: fixed;
                right: 0;
                left: 0;
                border-width: 0 0 1px;
           }
           header {
                height: 60px;
                background-color: #3d4450;
                border-color: #080808;
                line-height: 50px; # 居中
           }
           header nav a {
                color: #fff;
                padding: 0 1.5rem 0 1.5rem; # 导航分类间距(padding: 上下左右)
           }
           header nav a:hover {
                color: #fff;
                text-decoration: none;
                background-color: #000; # 导航分类光标移动出现黑色背景
           }
           header a.log {
                font-size: 1.5rem;
                padding-left: 0;
           }
           header a.log:hover {
                background-color: #3d4450; # typeidea不出现黑色背景
           }
           /*主体部分,左侧右侧栏为白色背景*/
           <!--.main .left-side .inner {-->
                <!--background-color: #fff;-->
                <!--padding: 20px 10px;-->
           <!--}-->
           <!--.main .right-side .inner {-->
                <!--background-color: #fff;-->
           }
           .category a{
                padding-top: 20px;
                margin-right: 20px; # 导航分类之间的距离
           }
          .post-element-nav {
                padding-top: 0;
                padding-bottom: 0;
                color: #428bca;
          }
          .post-element-title {
                font-size: 25px;
                border-bottom: 1px solid #ccc; # 放下面a 就是标题下出现下划线
          }
          .post-element-title a{
                color: #333;
                text-decoration: none;
          }
          .post-element-desc {
                padding: 1rem;
          }
          .main {
                margin-top: 80px;
          }
          .main ul {
                padding-left: 0px;
          }
         .post-element article {
                margin-top: 10px; #
          }
         .by {
                margin-top: 40px;
          }
          .sidebar li {
                list-style: none;
          }
          .sidebar a {
                color: #444;
          }
          .sidebar-title {
                height: 30px;
                background-color: #3d4450;
                border-color: #080808;
                line-height: 30px;
                color: #fff;
                padding: 0 9px;
          }
          .sidebar-content {
                padding: 0 9px;
          }

      </style>
      <title>Treehl的博客</title>
  </head>
  <body>

  <header class="fixed-top">
      <div class="container">
          <div class="row">
                <nav class="nav">
                    <a class="log" href="/">Myblog</a>
                    <a class="index" href="/">首页</a>
                    {% for cate in nav_cates %}
                    <a class="link" href="{% url 'category' cate.id %}">{{ cate.name }}</a>
                    {% endfor %}
                </nav>
          </div>
      </div>
  </header>


    <div class="container main">
        <div class="row">
            <div class="col-8 left-side">
                <div class="inner">
                {% block content %}
                {% endblock %}
                </div>
            </div>
            <div class="col-3 right-side">
                <div class="inner">
                {% for side in sidebars %}
                <div class="sidebar">
                    <div class="sidebar-title">{{ side.title }}</div>
                    <div class="sidebar-content">
                        {% if side.display_type == 1 %}
                            {% autoescape on %}
                            {{ side.content }}
                            {% endautoescape %}
                        {% elif side.display_type == 2 %}
                        <ul>
                            {% for post in recently_posts %}
                            <li><a href="{% url 'detail' post.pk %}">{{ post.title }}</a></li>
                            {% endfor %}
                        </ul>
                        {% elif side.display_type == 3 %}
                        <ul>
                            {% for post in hot_posts %}
                            <li><a href="{% url 'detail' post.pk %}">{{ post.title }} - {{ post.pv }}</a></li>
                            {% endfor %}
                        </ul>
                        {% elif side.display_type == 4 %}
                        <ul>
                            {% for comment in recently_comments %}
                            <li>{{ comment.content }}</li>
                            {% endfor %}
                        </ul>

                        {% endif %}
                    </div>
                </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>

  <footer class="footer">
      <div class="container">
          <hr/>
          <nav class="nav category">
              {% for cate in cates %}
                <a href="{% url 'category' cate.id %}">{{ cate.name }}</a>
              {% endfor %}
          </nav>
      </div>
      <div class="container by">
          <span class="text-muted">Power by Myblog@treehl</span>
      </div>
  </footer>
  </body>
</html>

```

效果是这样的

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/Q5m.6DV0ZtIv6gtHMsSu7M9Y7FTEMSciVr.xnUON4SQ!/b/dFYBAAAAAAAA&bo=awcTAwAAAAADB14!&rf=viewer_4)


[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)

