
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# HOME PAGE
def home(request):
    return render(request, 'foodwise/home.html')


# REGISTRATION
def register_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Registration successful! Please login.'
            )

            return redirect('login')

    else:
        form = UserCreationForm()

    return render(
        request,
        'foodwise/register.html',
        {'form': form}
    )
# DASHBOARD
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'foodwise/dashboard.html')


# FOOD MENU
@login_required(login_url='login')
def menu(request):
    return render(request, 'foodwise/menu.html')


# CALORIE CALCULATOR
@login_required(login_url='login')
def calorie_calculator(request):
    return render(request, 'foodwise/calorie_calculator.html')


# FOOD RECOMMENDATIONS
@login_required(login_url='login')
def recommendations(request):
    return render(request, 'foodwise/recommendations.html')


# NUTRITION DASHBOARD
@login_required(login_url='login')
def nutrition(request):
    return render(request, 'foodwise/nutrition.html')


# CHATBOT
@login_required(login_url='login')
def chatbot(request):
    return render(request, 'foodwise/chatbot.html')
