from lib2to3.pgen2.token import OP
from django.contrib import admin
from .models import Restaurant, Recept

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Recept)
