from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Dish, Comment
from .forms import CommentForm
from django.contrib.auth import login, authenticate


def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    comments = dish.comments.all()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You need to login to comment.")
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.dish = dish
            comment.save()
            messages.success(request, "Comment added successfully!")
            return redirect('dish_detail', dish_id=dish.id)
        else:
            messages.error(request, "Error in adding comment.")
    else:
        form = CommentForm()
    return render(request, 'dish_detail.html', {'dish': dish, 'comments': comments, 'form': form})


from django.shortcuts import render
from .models import Dish

def list_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'list_dishes.html', {'dishes': dishes})
