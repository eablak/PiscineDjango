import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.username = self.scope['user'].username
        user = self.scope['user']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        if user.is_authenticated:
            await self.accept()

            await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_joined',
                'username': self.username
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
            'username': event['username']
        }))