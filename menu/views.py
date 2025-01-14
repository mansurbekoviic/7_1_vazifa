from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Dish
from .forms import CategoryForm, DishForm
from django.db.models import Q
from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def all_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'all_dishes.html', {'dishes': dishes})

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'dish_detail.html', {'dish': dish})

def category_dishes(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    dishes = category.dishes.all()
    return render(request, 'category_dishes.html', {'category': category, 'dishes': dishes})

def manage_dish(request, pk=None):
    dish = get_object_or_404(Dish, pk=pk) if pk else None
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('all_dishes')
    else:
        form = DishForm(instance=dish)
    return render(request, 'manage_dish.html', {'form': form})

def manage_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk) if pk else None
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('all_dishes')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'manage_category.html', {'form': form})

def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    dish.delete()
    return redirect('all_dishes')

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('all_dishes')

def search_dishes(request):
    query = request.GET.get('q', '')
    dishes = Dish.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search_results.html', {'dishes': dishes, 'query': query})
