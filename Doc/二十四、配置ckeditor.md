---
title: 配置ckeditor
date: 2018-4-8 20:08:08
tags:
- Django
- Ckeditor
---
### **二十四、配置ckeditor**
官网地址
https://ckeditor.com/ckeditor-5-builds/

> pip install ckeditor

这一节主要有三点学习内容：
- 简单配置出ckeditor
- 上传图片功能
- 给图片加上水印


**一、简单配置ckeditor**
先在settings/base.py INSTALLED_APP中注册ckeditor
```python
# base.py

'ckeditor',


```


接下来在adminforms.py中重写content


```python
# adminforms.py
from ckeditor.widgets import CKEditorWidget

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), label='正文', required=True)

```

这样配置完成后，在ckeditor编辑框中有可能输入内容无法显示到页面，这里需要修改markdown的model层，加上else语句，如果不是markdown就返回正常内容


```python
# blog/models.py


    def save(self, *args, **kwargs):
        if self.is_markdown:
            self.html = markdown.markdown(
                self.content, extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                ]
            )
        else:
            self.html = self.content
        return super(Post, self).save(*args, **kwargs)

```

**二、增加上传图片功能**

首先还是在settings/base.py中注册ckeditor_uploader，再写入ckeditor的配置信息
```python
# 

'ckeditor_uploader',



CKEDITOR_RESTRICY_BY_USER = True
CKEDITOR_UPLOAD_PATH = 'content/ckeditor'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```



重新编写adminforms中的widget

```python
# adminforms.py

from ckeditor_uploader.widgets import CKEditorUploadingWidget

 content = forms.CharField(
        widget=CKEditorUploadingWidget(), label="内容"
    )

```


加上url

```python
# urls.py

from ckeditor_uploader import urls as uploader_urls
from django.conf.urls.static import static
from django.conf import settings




  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



```

好了，试着穿上图片到文章内吧！！




**三、图片上水印**

安装pillow来帮助我们处理图片

> pip install pillow



在Myblog目录下新建storage.py， font-family是字体路径，可以下载一个放在本地


```python
# storage.py



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.six import StringIO
from PIL import Image, ImageDraw, ImageFont


class MyStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        # 处理逻辑
        if 'image' in content.content_type:
            # 加水印
            image = self.watermark_with_text(content, 'Treehl', 'black')
            content = self.convert_image_to_file(image, name)

        return super(MyStorage, self).save(name, content, max_length=max_length)

    def convert_image_to_file(self, image, name):
        temp = StringIO()
        image.save(temp, format='PNG')
        return InMemoryUploadedFile(temp, None, name, 'image/png', temp.len, None)

    def watermark_with_text(self, file_obj, text, color, fontfamily='C:/Users/ssaw/Downloads/font1372/Xolonium-Regular.ttf'):
        image = Image.open(file_obj).convert('RGBA')
        imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

        draw = ImageDraw.Draw(imageWatermark)
        width, height = image.size
        margin = 10
        font = ImageFont.truetype(fontfamily, int(height / 20))
        textWidth, textHeight = draw.textsize(text, font)
        x = (width - textWidth - margin) / 2
        y = height - textHeight - margin

        draw.text((x, y), text, color, font)

        return Image.alpha_composite(image, imageWatermark)


```

接下来把DEFAULT_FILE_STORAGE = 'Myblog.storage.MyStorage'加入base.py中


```python
# base.py



DEFAULT_FILE_STORAGE = 'Myblog.storage.MyStorage'


```


好了，运行下服务，效果如下



![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/ARCxAVHdgQQw.QNnTiCEt8sqEr57wCwEo7bD8.C9Seo!/b/dDMBAAAAAAAA&bo=wAb1AgAAAAADBxM!&rf=viewer_4)





[GitHub](https://github.com/Family-TreeSY/Myblog)
欢迎访问[Treehl的博客](https://family-treesy.github.io/)


