from django.contrib import admin
from django.urls import path, include
from menu import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', views.home, name='home'),  
    path('dishes/', include('menu.urls')),  
]
