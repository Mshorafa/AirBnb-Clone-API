from rest_framework import serializers
from users.serializer import TinyUser
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    user = TinyUser()
    class Meta:
        model = Room
        fields = ['name', 'price', 'beds', 'instant_book', 'user']
