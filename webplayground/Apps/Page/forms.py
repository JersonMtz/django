from django import forms
from Apps.Page.models import *

class FormPages(forms.ModelForm):

    class Meta:
        model = Pages
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden'}),
        }

        labels = {
            'title':'', 'order':'', 'content': ''
        }