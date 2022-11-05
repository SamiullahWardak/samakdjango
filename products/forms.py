from cgi import print_exception
from dataclasses import fields
from django import forms

from .models import product

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'myName'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'samak' in title:
            raise forms.ValidationError('This is not a valid title!')
        if not 'news' in title:
            raise forms.ValidationError('This is not a valid title!')
        return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not '@gmail' in email:
            raise forms.ValidationError('This is not a valid email!')
        
class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField()
    price       = forms.CharField()
    email       = forms.EmailField()
