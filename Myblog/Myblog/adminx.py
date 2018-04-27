# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from xadmin.views import CommAdminView


class BaseOwnerAdmin(object):
    def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin, self).get_list_queryset()
        # 是超级用户返回qs
        if request.user.is_superuser:
            return qs
        # 不是返回自己用户
        return qs.filter(owner=request.user)

    def save_models(self):
        # import pdb;pdb.set_trace()
        if not self.org_obj:
            self.new_obj.author = self.request.user
        return super(BaseOwnerAdmin, self).save_models()


class GlobalSetting(CommAdminView):
    """后台设置"""
    site_title = 'Myblog'
    site_footer = 'power by MyBlog@treehl'


xadmin.site.register(CommAdminView, GlobalSetting)
