from django.urls import path

from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('add/', views.add_product, name='add_product'),

    path('delete/<int:id>/', views.delete_product, name='delete_product'),

    path('stockout/<int:id>/', views.stock_out, name='stock_out'),

    path('restock/<int:id>/', views.create_restock, name='create_restock'),

    path('restock/', views.restock_list, name='restock_list'),

    path('approve/<int:id>/', views.approve_restock, name='approve_restock'),

    path('reject/<int:id>/', views.reject_restock, name='reject_restock'),
]