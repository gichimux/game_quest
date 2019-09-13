from django import forms
from .models import Tournament,Profile

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        exclude = ['']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
