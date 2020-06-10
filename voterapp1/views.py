# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def check_vote_eligibility(request):
    n = 10
    if n > 18:
        return HttpResponse('<h1 style="color:green;"> You are eligible for vote </h1>')
    else:
        return HttpResponse('<h1 style="color:red;"> You are not eligible for vote </h1>')
        
