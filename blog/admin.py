# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from blog.models import Artikel, Penulis, Kategori

# Register your models here.

admin.site.register(Artikel)
admin.site.register(Penulis)
admin.site.register(Kategori)




