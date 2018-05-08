# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms


class SideBarAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea, label="内容", required=False
    )
