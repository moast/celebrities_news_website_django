# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1> This is the Blog Section of my website </h1>")