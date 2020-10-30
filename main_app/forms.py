from django import forms
from .models import Spotting, Bird

class SpottingForm(forms.ModelForm):
    class Meta:
        model = Spotting
        fields = ['date' , 'location' , 'time_of_day']

class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ('species' , 'likes' , 'native_to')