from rest_framework import serializers

from .models import Recept, Restaurant


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("name", "category", "adres", "city", "zip_code", "phone")


class ReceptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recept
        fields = (
            "pk",
            "name",
            "description",
            "ingredients",
            "persons",
            "preperation_time",
            "image",
        )
