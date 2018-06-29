from django import forms
from .models import Profiles

class ProfilesForm(forms.Form):
    prefix_name = forms.CharField(label='prefix_name', max_length=50)
