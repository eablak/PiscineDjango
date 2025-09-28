from django.shortcuts import render
from . import models

# Create your views here.

def lobby(request):
    rooms = models.ChatRoom.objects.all().values_list("name", flat=True)
    return render(request, 'lobby.html', context={"rooms":rooms})

def room(request, room_name):
    rooms = models.ChatRoom.objects.get(name=room_name)
    return render(request, 'chat.html', context={"room_name":room_name})