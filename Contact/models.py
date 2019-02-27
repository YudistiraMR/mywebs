# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=50)
    twitter = models.CharField(max_length=20)
    github = models.CharField(max_length=20)
    no_hp = models.IntegerField()

    def __unicode__(self):
        return self.email