from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Dish
from .forms import CategoryForm, DishForm
from django.contrib import messages


def home(request):
    return render(request, 'menu/home.html')

def all_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/all_dishes.html', {'dishes': dishes})

def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    return render(request, 'menu/dish_detail.html', {'dish': dish})

def category_dishes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    dishes = category.dishes.all()
    return render(request, 'menu/category_dishes.html', {'category': category, 'dishes': dishes})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category qo'shildi!")
            return redirect('all_dishes')
    else:
        form = CategoryForm()
    return render(request, 'menu/add_category.html', {'form': form})

def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dish qo'shildi!")
            return redirect('all_dishes')
    else:
        form = DishForm()
    return render(request, 'menu/add_dish.html', {'form': form})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category yangilandi!")
            return redirect('all_dishes')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'menu/edit_category.html', {'form': form})

def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            messages.success(request, "Dish yangilandi!")
            return redirect('all_dishes')
    else:
        form = DishForm(instance=dish)
    return render(request, 'menu/edit_dish.html', {'form': form})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, "Category o'chirildi!")
    return redirect('all_dishes')

def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    dish.delete()
    messages.success(request, "Dish o'chirildi!")
    return redirect('all_dishes')
