from django.urls import path
from . import views

urlpatterns = [
    path('dishes/', views.all_dishes, name='all_dishes'),
    path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),

]
