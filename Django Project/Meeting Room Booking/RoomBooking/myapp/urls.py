from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('addRoom/', views.addRoom, name='addRoom'),
    path('viewBooking/', views.viewBooking, name='viewBooking'),
    path('bookingRoom/<int:id>/', views.bookingRoom, name='bookingRoom'),
    path('cancel/<int:id>/', views.cancel, name='cancel'),

]