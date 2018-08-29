---
title: Django博客迁移至Python3
date: 2018-08-29 21:08:08
tags:
- Python
- Django
---
#### **迁移至Python3**


这里我们把项目迁移至Python3

新建python3虚拟环境

> python -m venv myblog-env3

激活虚拟环境
> source bin/activate


接下来安装项目所需要的包，这里发现一个新技能，之前我们用setup.py打包了项目，我们可以将需要安装的包放入install_requires里，然后修改requirements.txt

这里面要提醒下，xadmin需要用git去装，不然会出现版本冲突，所以xadmin就不要放入install中了，后面单独手动安装

> pip install git+https://github.com/the5fire/django-xadmin.git

```python
# requirements.txt
# 意思是从setup.py中寻找

-e .

```


```python
# setup.py

 install_requires=[
        'asn1crypto==0.24.0',
        'autopep8==1.3.4',
        'backports.shutil-get-terminal-size==1.0.0',
        'bcrypt==3.1.4',
        'certifi==2018.1.18',
        'cffi==1.11.5',
        'chardet==3.0.4',
        'colorama==0.3.9',
        'coreapi==2.3.3',
        'coreschema==0.0.4',
        'cryptography==2.2.2',
        'decorator==4.2.1',
        'diff-match-patch==20121119',
        'Django==1.11.3',
      .............
      .............
      .............

```


所有包安装完毕后就运行下试试看，应该不会有太大问题，如果缺包就需要手动再安装

> python manage.py runserver

最后，几个app的model需要将____unicode____改为____str____，Python3并不支持___unicode____





欢迎访问[Treehl的博客](https://family-treesy.github.io/)

[GitHub](https://github.com/Family-TreeSY)



