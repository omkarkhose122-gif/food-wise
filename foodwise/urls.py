
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path(
        'calorie-calculator/',
        views.calorie_calculator,
        name='calorie_calculator'
    ),

    path(
        'recommendations/',
        views.recommendations,
        name='recommendations'
    ),

    path('menu/', views.menu, name='menu'),

    path('nutrition/', views.nutrition, name='nutrition'),
]
