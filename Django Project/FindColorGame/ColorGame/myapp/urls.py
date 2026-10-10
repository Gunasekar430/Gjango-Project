from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save-result/', views.save_result, name='save_result'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]