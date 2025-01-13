from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Dish
from .forms import CategoryForm, DishForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
def home(request):
    return render(request, 'menu/home.html')

@login_required
def all_dishes(request):
    dishes = Dish.objects.all()
    can_change_dish = request.user.has_perm('menu.change_dish')
    can_delete_dish = request.user.has_perm('menu.delete_dish')
    return render(request, 'menu/all_dishes.html', {
        'dishes': dishes,
        'can_change_dish': can_change_dish,
        'can_delete_dish': can_delete_dish,
    })
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

from django.core.mail import send_mail
@login_required
@permission_required('menu.add_dish', raise_exception=True)
def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save()
            send_mail(
                subject='Yangi Dish qo\'shildi',
                message=f"Yangi dish qo'shildi: {dish.name}. Narxi: {dish.price}",
                from_email='djamoldinovmuhammadali571@gmail.com',
                recipient_list=['recipient_email@gmail.com'],
                fail_silently=False,
            )
            return redirect('all_dishes')
    else:
        form = DishForm()
    return render(request, 'menu/add_dish.html', {'form': form})

@login_required
@permission_required('menu.change_dish', raise_exception=True)
def edit_dish(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('all_dishes')
    else:
        form = DishForm(instance=dish)
    return render(request, 'menu/edit_dish.html', {'form': form, 'dish': dish})

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
@login_required
@permission_required('menu.delete_dish', raise_exception=True)
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    dish.delete()
    messages.success(request, "Dish o'chirildi!")
    return redirect('all_dishes')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dishes/')
        else:
            return render(request, 'registration/login.html', {'error': 'Login yoki parol noto‘g‘ri!'})
    return render(request, 'registration/login.html')