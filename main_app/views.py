from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Bird, Habitat
from .forms import SpottingForm, BirdForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# ---------------------------------------- STATIC PAGES
#HOME VIEW
def home(request):
    return render(request, 'home.html')


#ABOUT VIEW
def about(request):
    return render(request, 'about.html')


# ---------------------------------------- BIRDS
# BIRD INDEX
def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})


# BIRD DETAILS 
def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    habitats_bird_doesnt_have = Habitat.objects.exclude(id__in = bird.habitats.all().values_list('id'))
    spotting_form = SpottingForm()

    return render(request, 'birds/detail.html', {
        'bird': bird,
        'spotting_form': spotting_form,
        'habitats': habitats_bird_doesnt_have
        })

def add_bird(request):
    if request.method == 'POST':
        bird_form = BirdForm(request.POST)
        if bird_form.is_valid():
            new_bird = bird_form.save(commit=False)
            new_bird.user = request.user
            new_bird.save()

            return redirect('detail', new_bird.id)
    else:
        form = BirdForm()
        context = {'form': form}
        return render(request, 'birds/new.html', context)


def delete_bird(request, bird_id):
    Bird.objects.get(id=bird_id).delete()
    return redirect('index')


def edit_bird(request, bird_id):
    bird = Bird.objects.get(id=bird_id)

    if request.method == 'POST':
        bird_form = BirdForm(request.POST, instance=bird)
        if bird_form.is_valid():
            updated_bird = bird_form.save()
            return redirect('detail', updated_bird.id)
    else:
        form = BirdForm(instance=bird)
        context = {'form': form}
        return render(request, 'birds/edit.html', context)

# ---------------------------------------- HABITATS
# ADD HABITAT
def assoc_habitat(request, bird_id, habitat_id):
    Bird.objects.get(id=bird_id).habitats.add(habitat_id)
    return redirect('detail', bird_id=bird_id)


def remove_habitat(request, bird_id, habitat_id):
    Bird.objects.get(id=bird_id).habitats.remove(habitat_id)
    return redirect('detail', bird_id=bird_id)


# ---------------------------------------- BIRD SPOTTINGS
# ADD A SPOTTING
def add_spotting(request, bird_id):
    form = SpottingForm(request.POST)

    if form.is_valid():
        #don't save the form to the db until it is validated
        new_spotting = form.save(commit=False)
        new_spotting.bird_id = bird_id
        new_spotting.save()
        #ALWAYS REDIRECT, not render, when changing data in the db
    return redirect('detail', bird_id=bird_id)


#AUTH
def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'invalid credentials. Please check your username/password and try again.'
    form = UserCreationForm()
    context = {'form':form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)