from django import forms

from . import models

class MDForm (forms.ModelForm):
    class Meta:
        model = models.EditBlog
        fields = ['name', 'text']
        labels = {'name ': 'Title', 'text': ''}
