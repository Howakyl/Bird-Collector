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
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {'bird': bird})