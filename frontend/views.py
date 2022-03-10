import random

from django.views.generic import View
from django.shortcuts import render

from backend.api import get_recepy_json, get_restaurant_json

# Create your views here
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {"recepten": random.choice(get_recepy_json()), "restaurant": random.choice(get_restaurant_json())}
        return render(request, "home_view.html", context)

class HelpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "help_view.html")

class OpgeslagenView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "opgeslagen_view.html")