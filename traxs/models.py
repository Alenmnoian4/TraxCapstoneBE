from django.db import models

class Trax(models.Model):
    name = models.CharField(max_length=100)
    workout = models.CharField(max_length=100)
    meal = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)