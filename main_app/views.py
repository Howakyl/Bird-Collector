from django.shortcuts import render

from django.http import HttpResponse

#HOME VIEW
def home(request):
    return HttpResponse('<h1>hello!</h1>')
