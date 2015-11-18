# coding: utf-8

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
__author__ = 'mironnn'


@login_required(login_url='login/')
def index(request):
    return render(request, "index.html")


@login_required(login_url='login/')
def show_map(request):
    return render(request, "office_map.html")
    # return HttpResponse('ok')

