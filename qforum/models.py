# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    views = models.PositiveIntegerField()


class Post(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    votes = models.PositiveIntegerField
    views = models.PositiveIntegerField
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    post = models.ForeignKey(Post, models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    votes = models.PositiveIntegerField()
    parent = models.ForeignKey('self')

    def __str__(self):
        return self.user + ": " + self.content
