from django.shortcuts import render
# from django.http import HttpResponse
from .models import Bird

#HOME VIEW
def home(request):
    return render(request, 'home.html')

#ABOUT VIEW
def about(request):
    return render(request, 'about.html')

# BIRD INDEX
def birds_index(request):
    return render(request, 'birds/index.html', {'birds': birds})
