from django import forms 

from .models import Category, Link

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)