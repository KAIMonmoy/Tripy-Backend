from rest_framework import serializers

from core.models import *
from user.serializers import CustomUserSerializer


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    room_set = RoomSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = "__all__"
