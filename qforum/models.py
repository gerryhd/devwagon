# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=120)
    tags = models.ManyToManyField
    interest = models.PositiveIntegerField
    views = models.PositiveIntegerField
    

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name