# -*- coding: utf-8 -*-
from django.http import HttpResponse
#from __future__ import unicode_literals

#from django.shortcuts import render
def index(request):
    return HttpResponse("Hello Sinar.. How are you ?.")
# Create your views here.
