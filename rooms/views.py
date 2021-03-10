from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models,serializer


# Create your views here.

@api_view(['GET'])
def list_rooms(request):
    rooms = models.Room.objects.all()
    serialized_room  = serializer.RoomSerializer(rooms,many=True)
    return Response(data=serialized_room.data)
