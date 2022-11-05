from dataclasses import fields
from pyexpat import model
from django import forms
from blog.models import Article

class BlogForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
