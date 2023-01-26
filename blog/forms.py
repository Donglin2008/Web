from django import forms

from . import models

class MDForm (forms.ModelForm):
    class Meta:
        model = models.EditBlog
        fields = ['name', 'preface', 'text']
        labels = {'name ': '标题: ', 'preface': '序言: ', 'text': '正文: '}
        widgets = {'preface': forms.Textarea(attrs={'rows': 5, 'cols': 50, 'id': 'preface','class': 'form-control'})}
