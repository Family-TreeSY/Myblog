"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

import xadmin
from xadmin.plugins import xversion
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from blog.views import (
    IndexView, CategoryView, TagView, PostView, AuthorView
)
from config.views import LinkView
from comment.views import CommentView
from .autocomplete import CategoryAutocomplete, TagAutocomplete
from blog.api import PostViewSet, CategoryViewSet, TagViewSet


xadmin.autodiscover()
xversion.register_models()

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)/$',
        CategoryView.as_view(), name="category"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="detail"),
    url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name="author"),
    url(r'^links/$', LinkView.as_view(), name="links"),
    url(r'^comment/$', CommentView.as_view(), name="comment"),
    url(r'^admin/', xadmin.site.urls),
    url(r'^category-autocomplete/$',
        CategoryAutocomplete.as_view(),
        name='category-autocomplete'),
    url(r'^tag-autocomplete/$',
        TagAutocomplete.as_view(),
        name='tag-autocomplete'),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title="Myblog API")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
