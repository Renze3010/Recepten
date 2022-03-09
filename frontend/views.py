from django.views.generic import View
from django.shortcuts import render

# Create your views here
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home_view.html")
