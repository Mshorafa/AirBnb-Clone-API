from  rest_framework.generics import ListAPIView
from . import models, serializer
from .models import Room


# Create your views here.


class ListRoomsView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = serializer.RoomSerializer

