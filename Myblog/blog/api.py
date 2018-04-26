# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rest_framework import serializers, viewsets, pagination

from .models import Post, Category, Tag


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

    created_time = serializers.DateTimeField(
        # year-month-date hour:minute:second
        format="%Y-%m-%d %H:%M:%S"
    )

    class Meta:
        model = Post
        fields = (
             'url', 'title', 'pv', 'uv',
             'author', 'category', 'tag', 'created_time',
        )


class PostDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(
        read_only=True,
        )

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'desc', 'posts',
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super(PostViewSet, self).retrieve(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(PostViewSet, self).get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
             'url', 'name', 'status', 'author', 'created_time',
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(
        many=True,
        read_only=True,
        )

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'author', 'post_set',
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=1)
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super(CategoryViewSet, self).retrieve(request, *args, **kwargs)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
             'url', 'name', 'status', 'author', 'created_time',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(
    #     many=True,
    #     read_only=True,
    #     )
    posts = serializers.SerializerMethodField('paginated_posts')

    # 分页
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
             'id', 'url', 'username',
        )


class UserDetailSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id', 'username', 'post_set',
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = UserDetailSerializer
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)
