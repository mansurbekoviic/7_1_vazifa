from django import forms
from .models import Category, Dish

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'category']
