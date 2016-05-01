from django.shortcuts import render

from .models import Nutron_Food, Nutron_User


# Create your views here.
def get_users(request):
    users = Nutron_User.objects.all()
    return render(request, 'get_users.html', {'users': users})


def get_foods(request):
    foods = Nutron_Food.objects.all()
    return render(request, 'get_foods.html', {'foods': foods})


def home(request):
    return render(request, 'home.html', {})


def new_user(request):
    return render(request, 'home.html', {})


def new_food(request, name, calorific_value, diabetes, hypertension, anemia, high_cholesterol):
    f = Nutron_Food
    f.diabetes = diabetes
    f.calorific_value = calorific_value
    f.high_cholesterol = high_cholesterol
    f.anemia = anemia
    f.name = name
    f.hypertension = hypertension
    f.save()

    return render(request, 'home.html', {})
