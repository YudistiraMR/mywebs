# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from .models import Artikel
# Create your views here.
def index(request):
	nama = "Yudistira"
	buah = ['Jeruk','Apel','Melon','Kesemek']
	return render(request,'layout/index.html',{'nama':nama,'buah' : buah})
def about(request):
	return render(request,'layout/about.html')
def contact(request):
	return render(request,'layout/kontak.html')
def blog(request):
	blogs = Artikel.objects.filter(publish=True)
	return render(request,'layout/blog.html',{'blogs':blogs})