from pyexpat import model
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    adres = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)

class Recept(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    persons = models.CharField(max_length=60)
    preperation_time = models.CharField(max_length=25)