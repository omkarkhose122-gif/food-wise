
from django.shortcuts import render


def home(request):
    return render(request, 'foodwise/home.html')


def dashboard(request):
    return render(request, 'foodwise/dashboard.html')


def calorie_calculator(request):
    result = None

    if request.method == 'POST':
        try:
            age = int(request.POST.get('age'))
            weight = float(request.POST.get('weight'))
            height = float(request.POST.get('height'))
            gender = request.POST.get('gender')
            activity = float(request.POST.get('activity'))

            if age <= 0 or weight <= 0 or height <= 0:
                raise ValueError

            if gender == 'male':
                bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
            elif gender == 'female':
                bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
            else:
                raise ValueError

            result = round(bmr * activity)

        except (ValueError, TypeError):
            result = 'Please enter valid details.'

    return render(request, 'foodwise/calorie_calculator.html', {
        'result': result
    })


def recommendations(request):
    return render(request, 'foodwise/recommendations.html')


def menu(request):
    return render(request, 'foodwise/menu.html')


def nutrition(request):
    return render(request, 'foodwise/nutrition.html')
