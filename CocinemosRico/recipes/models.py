from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=250)
    recipe = models.CharField(max_length=1000)

