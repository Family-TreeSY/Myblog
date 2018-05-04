---
title: 使用Nginx和Gunicorn部署网站
date: 2018-4-8 23:30:08
tags:
- Django
---
### **三十、使用Nginx和Gunicorn部署网站**

> 部署项目会遇到很多问题，即使完全照着教程来也会有问题，务必要有十足的耐心啃下来。部署这一小节，切换到windows系统用xshell远程连接ubuntu服务器

**项目部署我参考了[追梦人的博客](https://www.zmrenwu.com/post/20/)，这里只记录一些需要注意的问题，当时Django入门学习完官方的教程后，我就照着这位大佬的博客写了一遍，非常棒的教程**


1. 购买域名
这里我用的是[阿里云](https://wanwang.aliyun.com/?spm=5176.8142029.388261.277.54216d3enJjhf1)，最便宜的只要4块钱，购买后只要通过验证，再按着教程解析域名就可以了，
2. 购买服务器
这里我用的是[vultr](https://www.vultr.com/)，附上[搭建教程](https://www.flyzy2005.com/fan-qiang/shadowsocks/install-shadowsocks-in-one-command/)，从此上网畅通无阻
3. 代码上传GitHub
在github上创建代码仓库后，方便我们拉取代码到服务器，服务器上拉取代码需要git的钥匙，不然会有权限错误的报错，git教程可以查看[廖雪峰的Git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)，花一天的时间就可以学完，
4. vim简单命令
部署过程种，需要写nginx配置信息，这里举个例子，我们要创建一个test文件
> vim test

进入界面后需要按一下i键，就进入写入模式

内容写完后，我们要保存退出，先按ESC键，再输入:wq(写入，退出的意思)

这里不出意外应该会出现文件只能读不能写的权限问题，这里要用到简单的linux权限命令
linux部分文件有rwx三个权限，分别代表4、2、1，777就代表文件所有者、同用户组、其他非本用户组的权限都是rwx，建议看下鸟哥的linux私房菜
- r(read)
- w(write)
- x(execute)
> chmod 777 test




[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)













