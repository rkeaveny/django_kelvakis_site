from django import forms
from .models import Baser

class InputForm(forms.ModelForm):
  name = forms.CharField(
    max_length=100,
    help_text='Please enter your name or name of database author'
    )
  subject = forms.CharField(
    max_length=100,
    help_text='Please enter the STEM field that your database is'
  )
  link = forms.URLField()
  description = forms.CharField(
    max_length=2000,
    widget=forms.Textarea(),
    help_text='What is this database?'
    )

  class Meta:
        model = Baser
        fields = ('name', 'subject', 'link', 'description')
