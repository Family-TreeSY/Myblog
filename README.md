---
title: Django学习小结
date: 2018-3-31 23:08:08
tags:
- Django
---

### Django学习小结
> 用Django搭建博客

![](https://img.shields.io/badge/Python-2.7-brightgreen.svg) ![](https://img.shields.io/badge/Django-1.11.3-green.svg) ![](https://img.shields.io/badge/xadmin-0.6.1-yellowgreen.svg) ![](https://img.shields.io/badge/ckedior-4.7.1-yellow.svg) ![](https://img.shields.io/badge/Django--debug--toolbar-2.0-orange.svg)
![](https://img.shields.io/badge/Django--silk-2.0-red.svg) ![](https://img.shields.io/badge/Redis-4.0.9-lightgrey.svg) ![](https://img.shields.io/badge/MySQL-5.7.21-blue.svg) ![](https://img.shields.io/badge/Bootstrap-4.1.0-brown.svg)
### 简介

- 项目主要是记录学习Django的过程
- 前端使用Bootstrap框架并没有套模板，自己画页面会丑点，最主要是简单学习下前端，在W3SCHOOL上学习了HTML和CSS的可以练练手
- 后台管理一开始先开发Django自带的admin到后面会转到Xadmin上
- 视图先用FunctionView来写逻辑，后面再使用ClassBasedView
- 数据库在开发环境中先使用SQLITE，最后准备上线前替换为MySQL数据库
- 文本编辑使用Ckeditor富文本编辑
- 使用Django-Rest-Framework来构建Web API
- 使用Django-debug-toolbar和silk来分析检查
- 配置MySQL和开发环境
- 配置Redis
- 使用Nginx和Gunicorn部署网站
- 使用Fabric自动化部署




### 环境
- 开发语言：Python2.7
- 开发环境:Ubuntu16.04
- IDE:Pycharm
- 数据库:MySQL、Redis

### 代码风格
- [谷歌开源项目风格](http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents/)
- 用flake8来检测代码

### 项目分四大块
- 后台admin开发
- 前台开发
- 增加功能插件
- 部署项目

**一、后台admin开发**

[1、搭建开发环境](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%B8%80%E3%80%81%E6%90%AD%E5%BB%BA%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83.md)
[2、建立博客应用](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E3%80%81%E5%BB%BA%E7%AB%8B%E5%8D%9A%E5%AE%A2%E5%BA%94%E7%94%A8.md)
[3、创建数据库模型Model](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%B8%89%E3%80%81%E5%88%9B%E5%BB%BA%E6%95%B0%E6%8D%AE%E5%BA%93%E6%A8%A1%E5%9E%8BModel.md)
[4、创建后台管理账号、迁移数据库](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%9B%9B%E3%80%81%E5%88%9B%E5%BB%BA%E5%90%8E%E5%8F%B0%E7%AE%A1%E7%90%86%E8%B4%A6%E5%8F%B7%E3%80%81%E8%BF%81%E7%A7%BB%E6%95%B0%E6%8D%AE%E5%BA%93.md)
[5、开发后台管理（一）](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%94%E3%80%81%E5%BC%80%E5%8F%91%E5%90%8E%E5%8F%B0%E7%AE%A1%E7%90%86%EF%BC%88%E4%B8%80%EF%BC%89.md)
[6、开发后台管理（二）](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%85%AD%E3%80%81%E5%BC%80%E5%8F%91%E5%90%8E%E5%8F%B0%E7%AE%A1%E7%90%86%EF%BC%88%E4%BA%8C%EF%BC%89.md)

**二、前台开发**

[1、FunctionView](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%B8%83%E3%80%81FunctionView.md)
[2、分页设置](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%85%AB%E3%80%81%E5%88%86%E9%A1%B5%E8%AE%BE%E7%BD%AE.md)
[3、设置分类导航栏](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%B9%9D%E3%80%81%E8%AE%BE%E7%BD%AE%E5%88%86%E7%B1%BB%E5%AF%BC%E8%88%AA%E6%A0%8F.md)
[4、设置侧边栏](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E3%80%81%E8%AE%BE%E7%BD%AE%E4%BE%A7%E8%BE%B9%E6%A0%8F.md)
[5、完成正文、配置通用代码](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E4%B8%80%E3%80%81%E5%AE%8C%E6%88%90%E6%AD%A3%E6%96%87%E3%80%81%E9%85%8D%E7%BD%AE%E9%80%9A%E7%94%A8%E4%BB%A3%E7%A0%81.md)
[6、ClassBasedView](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E4%BA%8C%E3%80%81ClassBasedView.md)
[7、使用BootStrap框架](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8BootStrap%E6%A1%86%E6%9E%B6.md)
[8、抽取静态资源](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E5%9B%9B%E3%80%81%E6%8A%BD%E5%8F%96%E9%9D%99%E6%80%81%E8%B5%84%E6%BA%90.md)
[9、增加搜索功能](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E4%BA%94%E3%80%81%E5%A2%9E%E5%8A%A0%E6%90%9C%E7%B4%A2%E5%8A%9F%E8%83%BD.md)
[10、增加作者文章列表](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E5%85%AD%E3%80%81%E5%A2%9E%E5%8A%A0%E4%BD%9C%E8%80%85%E6%96%87%E7%AB%A0%E5%88%97%E8%A1%A8.md)
[11、增加友链](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E4%B8%83%E3%80%81%E5%A2%9E%E5%8A%A0%E5%8F%8B%E9%93%BE.md)
[12、增加留言板模块（一）](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E5%85%AB%E3%80%81%E5%A2%9E%E5%8A%A0%E7%95%99%E8%A8%80%E6%9D%BF%E6%A8%A1%E5%9D%97%EF%BC%88%E4%B8%80%EF%BC%89.md)
[13、增加留言板模块（二）](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E5%8D%81%E4%B9%9D%E3%80%81%E5%A2%9E%E5%8A%A0%E7%95%99%E8%A8%80%E6%9D%BF%E6%A8%A1%E5%9D%97%EF%BC%88%E4%BA%8C%EF%BC%89.md)
[14、增加Markdown编辑](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E3%80%81%E5%A2%9E%E5%8A%A0Markdown%E7%BC%96%E8%BE%91.md)
[15、增加PV、UV功能](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E4%B8%80%E3%80%81%E5%A2%9E%E5%8A%A0PV%E3%80%81UV%E6%A8%A1%E5%9D%97.md)

**三、增加插件**

[1、admin替换为xadmin](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E4%BA%8C%E3%80%81admin%E6%9B%BF%E6%8D%A2%E4%B8%BAxadmin.md)
[2、配置autocomplete-light](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E4%B8%89%E3%80%81%E9%85%8D%E7%BD%AEautocomplete-light.md)
[3、配置ckeditor](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E5%9B%9B%E3%80%81%E9%85%8D%E7%BD%AEckeditor.md)
[4、配置Django-Rest-Framework](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E4%BA%94%E3%80%81%E9%85%8D%E7%BD%AEDjango-Rest-Framework.md)
[5、配置Django-Debug-ToolBar](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E5%85%AD%E3%80%81%E9%85%8D%E7%BD%AEDjango-Debug-ToolBar.md)
[6、二十七、配置Django-Silk](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E4%B8%83%E3%80%81%E9%85%8D%E7%BD%AEDjango-Silk.md)
[7、配置MySQL](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E5%85%AB%E3%80%81%E9%85%8D%E7%BD%AEMySQL.md)
[8、配置Cache Redis](https://github.com/Family-TreeSY/Myblog/blob/master/Doc/%E4%BA%8C%E5%8D%81%E4%B9%9D%E3%80%81%E9%85%8D%E7%BD%AECache%20Redis.md)

**四、部署项目**

[1、使用nginx和gunicorn部署网站]()
[2、使用Fabric自动部署]()

