from rest_framework import viewsets

from .serializers import ReceptSerializer, RestaurantSerializer
from .models import Restaurant, Recept


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer

class ReceptViewSet(viewsets.ModelViewSet):
    queryset = Recept.objects.all().order_by('name')
    serializer_class = ReceptSerializer