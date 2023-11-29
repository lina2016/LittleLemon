from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        extra_kwargs = {
            "no_of_guests": {"min_value": 1},
        }
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','title','price','inventory']
        extra_kwargs = {
            "price": {"min_value": 0},
            "inventory": {"min_value": 0},
        }