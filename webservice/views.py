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


def new_user(request, username, password, email, name, photo, level, score,
             age, height, weight, diabetes, hypertension, anemia, high_cholesterol):
    user = Nutron_User()
    user.username = username
    user.password = password
    user.email = email
    user.name = name
    user.photo = photo
    user.level = level
    user.score = score
    user.age = age
    user.weight = weight
    user.height = height
    user.diabetes = diabetes
    user.hypertension = hypertension
    user.anemia = anemia
    user.high_cholesterol = high_cholesterol
    user.save()
    return render(request, 'home.html', {})


def new_food(request, name, calorific_value, diabetes, hypertension, anemia, high_cholesterol):
    food = Nutron_Food()
    food.diabetes = diabetes
    food.calorific_value = calorific_value
    food.high_cholesterol = high_cholesterol
    food.anemia = anemia
    food.name = name
    food.hypertension = hypertension
    food.save()

    return render(request, 'home.html', {})
