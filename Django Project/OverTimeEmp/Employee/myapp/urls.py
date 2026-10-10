from django.contrib import admin
from django.urls import path,include
from .import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]