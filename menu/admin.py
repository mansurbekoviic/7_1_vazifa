from django.contrib import admin
from .models import Category, Dish, Comment

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Comment)