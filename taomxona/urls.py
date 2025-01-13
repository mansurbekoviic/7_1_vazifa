from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_dishes, name='home'),
    path('dishes/', views.all_dishes, name='all_dishes'),
    path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),
]
