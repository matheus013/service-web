# Create your models here.

from django.db import models
import json


class Nutron_User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    photo = models.CharField(max_length=50)
    level = models.IntegerField()
    score = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    diabetes = models.IntegerField()
    hypertension = models.IntegerField()
    anemia = models.IntegerField()
    high_cholesterol = models.IntegerField()

    def register(self):
        self.save()

    def toJson(self):
        return json.dumps({'username': self.username, 'password': self.password, 'email': self.email,
                           'name': self.name, 'photo': self.photo, 'level': self.level, 'score': self.score,
                           'age': self.age, 'height': self.height, 'weight': self.weight, 'diabetes': self.diabetes,
                           'hypertension': self.hypertension, 'anemia': self.anemia,
                           'high_cholesterol': self.high_cholesterol})

    def __str__(self):
        return self.username


class Nutron_Food(models.Model):
    name = models.CharField(max_length=30)
    calorific_value = models.IntegerField()
    diabetes = models.IntegerField()
    hypertension = models.IntegerField()
    anemia = models.IntegerField()
    high_cholesterol = models.IntegerField()

    def register(self):
        self.save()

    def toJson(self):
        return json.dumps({'name': self.name, 'diabetes': self.diabetes, 'calorific_value': self.calorific_value,
                           'hypertension': self.hypertension, 'anemia': self.anemia,
                           'high_cholesterol': self.high_cholesterol})

    def __str__(self):
        return self.name
