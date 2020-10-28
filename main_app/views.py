from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Bird
from .forms import SpottingForm

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
    spotting_form = SpottingForm()

    return render(request, 'birds/detail.html', {
        'bird': bird,
        'spotting_form': spotting_form
        })

def add_spotting(request, bird_id):
    form = SpottingForm(request.POST)

    if form.is_valid():
        #don't save the form to the db until it is validated
        new_spotting = form.save(commit=False)
        new_spotting.bird_id = bird_id
        new_spotting.save()
        #ALWAYS REDIRECT, not render, when changing data in the db
    return redirect('detail', bird_id=bird_id)