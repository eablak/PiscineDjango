import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from .models import *

async def get_last_three(room_name):
    chatroom = await sync_to_async(ChatRoom.objects.get)(name=room_name)

    last_three = await sync_to_async(
        lambda: list(
            UserMessage.objects.filter(room=chatroom)
            .select_related('username', 'room')
            .order_by('-timestamp')[:3]
        )
    )()

    json_last_tree = []
    for msg in last_three:
        # print(msg.message)
        # print(msg.username.username)
        
        json_last_tree.append({
            'message': msg.message,
            'username': msg.username.username
        })

    return json_last_tree



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.username = self.scope['user'].username
        self.user = self.scope['user']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        if self.user.is_authenticated:
            await self.accept()

            last_three = await get_last_three(self.room_name)

            await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_joined',
                'username': self.username,
                'last_three': last_three
            }
            )
   

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send (
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username': self.username
            }
        )

        await sync_to_async(UserMessage.objects.create)(
            username=self.user,
            message=message,
            room=await sync_to_async(ChatRoom.objects.get)(name=self.room_name)
        )


    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username': username
        }))

    async def user_joined(self, event):
        username = event['username']
        await self.send(text_data=json.dumps({
            'type': 'user-joined',
            'username': event['username'],
            'last_three': event.get('last_three', [])
        }))