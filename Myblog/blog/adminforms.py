# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms


class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label="是否删除", required=True)
    desc = forms.CharField(widget=forms.Textarea, label="摘要", required=False)

    def clean_status(self):
        # 读取name为status的表单提交值，并赋予status变量
        if self.cleaned_data["status"]:
            return 1
        else:
            return 2
