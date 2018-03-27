from django import forms
from .models import Baser

class InputForm(forms.ModelForm):
  name = forms.CharField(
    max_length=100,
    help_text='Please enter your name or name of database author'
    )
  field = forms.CharField(
    max_length=100,
    help_text='Please put the field of STEM the database falls under'
    )
  link = forms.URLField()
  description = forms.CharField(
    max_length=2000,
    widget=forms.Textarea(),
    help_text='What is this database?'
    )

  class Meta:
        model = Baser
        fields = ('name', 'field', 'link', 'description')
