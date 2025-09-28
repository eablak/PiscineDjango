from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/account")
def lobby(request):
    rooms = models.ChatRoom.objects.all().values_list("name", flat=True)
    return render(request, 'lobby.html', context={"rooms":rooms})

@login_required(login_url="/account")
def room(request, room_name):
    rooms = models.ChatRoom.objects.get(name=room_name)
    return render(request, 'chat.html', context={"room_name":room_name})