from django.shortcuts import render

from django.http import HttpResponse

#HOME VIEW
def home(request):
    return HttpResponse('<h1>hello!</h1>')

#ABOUT VIEW
def about(request):
    return HttpResponse('<h1>Let me tell ya about BIRDS.</h1>')
