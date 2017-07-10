# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render

from django.http import HttpResponse

from devwagon.apps.qforum.models import Post, Tag


def index(request):
    context_dict = {}

    return render(request, 'qforum/index.html', context_dict)

def blog(request):
    # tag = Tag(name="Python", views=5)
    # tag.save()
    # tag = Tag.objects.filter(name="Python")[0]
    # user = User.objects.get(username="Jhonny")
    # # user.save()
    # blog = Post(title="why do people still use php",
    #             content="I cant believe people are stil using such an awful language",
    #             votes=50,
    #             views=1000,
    #             user=user)
    # blog.save()
    # blog.tags.add(tag)
    blog_entries = Post.objects.all()
    return render(request, 'qforum/blog.html', {'blog_entries':blog_entries})