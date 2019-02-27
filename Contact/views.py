# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Contact
# Create your views here.
def contact(request):
    return render(request,'layout/kontak.html')
