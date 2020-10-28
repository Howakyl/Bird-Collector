from django import forms
from .models import Spotting

class SpottingForm(forms.ModelForm):
    class Meta:
        model = Spotting
        fields = ['date' , 'location' , 'time_of_day']