from django.contrib import admin
from django.urls import path,include
from .import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name = "main" ),
    path('delete/<id>/', views.delete, name = "delete" ),
    path('add/', views.add, name = "add" ),
    path('view/<id>/', views.view, name = "view" ),
    path('update/<id>/', views.update, name = "update" ),
]