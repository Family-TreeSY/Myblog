# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="内容",
        max_length=500,
        widget=forms.widgets.Textarea(
            attrs={
                "rows": 6,
                "cols": 88}))

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
