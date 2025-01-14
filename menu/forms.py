from django import forms
from .models import Category, Dish
from .validators import validate_positive

class DishForm(forms.ModelForm):
    price = forms.DecimalField(validators=[validate_positive])

    class Meta:
        model = Dish
        fields = ['name', 'category', 'description', 'price']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'category', 'description', 'price']
