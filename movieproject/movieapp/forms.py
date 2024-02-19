from django import forms
from . models import movie

class movieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','desc','year','img']