# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label="昵称",
        max_length=100,
        widget=forms.widgets.Input(
            attrs={
                'class': 'form-control',
                'style': 'width: 45%'}))

    email = forms.CharField(
        label="邮箱",
        max_length=100,
        widget=forms.widgets.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 45%'}))

    website = forms.CharField(
        label="站点",
        max_length=100,
        widget=forms.widgets.URLInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 45%'}))

    content = forms.CharField(
        label="内容",
        max_length=500,
        widget=forms.widgets.Textarea(
            attrs={
                "rows": 6,
                "cols": 88,
                "class": "form-control"}))

    def clean_content(self):
        """留言内容必须大于5个字符"""
        content = self.cleaned_data.get("content")
        if len(content) < 5:
            raise forms.ValidationError("写长一点噢！")
        return content

    class Meta:
        model = Comment
        fields = [
            "nickname", "email", "website", "content"
        ]
