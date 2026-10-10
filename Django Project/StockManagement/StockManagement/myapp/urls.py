from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name = 'main'),
    path('restock/<int:id>/', views.restock, name = 'restock'),
    path('add/', views.add, name = 'add'),
    path('purchase/<int:id>/', views.purchase, name = 'purchase'),
    path('delete/<int:id>/', views.delete, name = 'delete'),
]