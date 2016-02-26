# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    context          = {}
    context['label'] = 'app list'
    return render(request, 'index.html', context)