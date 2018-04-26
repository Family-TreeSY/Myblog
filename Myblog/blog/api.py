# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rest_framework import serializers, viewsets

from .models import Post, Category, Tag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
             'url', 'title', 'pv', 'uv',
             'author', 'category', 'tag', 'created_time',
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
             'url', 'name', 'status', 'author', 'created_time',
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=1)
    serializer_class = CategorySerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
             'url', 'name', 'status', 'author', 'created_time',
        )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(status=1)
    serializer_class = TagSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
             'id', 'username',
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer
