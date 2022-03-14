import random

from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from api.models import Opgeslagen, Recept
from backend.api import get_recepy_json, get_restaurant_json

# Create your views here
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {"recepten": random.choice(get_recepy_json()), "restaurant": random.choice(get_restaurant_json())}
        return render(request, "home_view.html", context)

class HelpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "help_view.html")

class OpgeslagenView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            "recepten": []
        }

        opgeslagen = Opgeslagen.objects.filter(userPK = request.user.pk)
        for item in opgeslagen:
            recept = Recept.objects.get(pk=item.receptPK)
            context["recepten"].append(recept)

        return render(request, "opgeslagen_view.html", context)

class OpslaanView(View):
    def post(self, request, *args, **kwargs):
        saved = Opgeslagen(userPK = request.user.pk, receptPK = request.POST.get("receptPK"))
        saved.save()

        return redirect("opgeslagen")

class DeleteView(View):
    def post(self, request, *args, **kwargs):
        Opgeslagen.objects.filter(pk=request.POST.pk).delete()

        return redirect("opgeslagen")