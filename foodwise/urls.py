
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Authentication
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='foodwise/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # FoodWise features
    path('menu/', views.menu, name='menu'),

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

    path('nutrition/', views.nutrition, name='nutrition'),

    path('chatbot/', views.chatbot, name='chatbot'),
]
