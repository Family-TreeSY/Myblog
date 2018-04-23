# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import redirect

from .forms import CommentForm
from comment.models import Comment


class CommonShowMixin(object):
    def get_comment(self):
        """获取评论再传递给模板"""
        target = self.request.path
        comments = Comment.objects.filter(target=target)
        return comments

    def get_context_data(self, **kwargs):
        kwargs.update({
            "comment_form": CommentForm,
            "comment_list": self.get_comment,
        })
        return super(CommonShowMixin, self).get_context_data(**kwargs)


class CommentView(TemplateView):
    template_name = "comment/result.html"

    def get(self, request, *args, **kwargs):
        return super(CommentView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        target = request.POST.get("target")
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False

        context = {
            "succeed": succeed,
            "form": comment_form,
            "target": target,
        }
        return self.render_to_response(context)
