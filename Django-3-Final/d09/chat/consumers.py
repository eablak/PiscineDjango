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
            
            await sync_to_async(ChatRoomUsers.objects.create)(
                user = self.user,
                room = await sync_to_async(ChatRoom.objects.get)(name=self.room_name)
            )
            userlist = await self.get_userlist()
            
            await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_joined',
                'username': self.username,
                'last_three': last_three,
                'userlist': userlist
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


    async def disconnect(self, code):

        user = await sync_to_async(User.objects.get)(username=self.username)
        room = await sync_to_async(ChatRoom.objects.get)(name=self.room_name)

        await sync_to_async(lambda: ChatRoomUsers.objects.filter(user=user, room=room).delete())()

        userlist = await self.get_userlist()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_disconnect',
                'username': self.username,
                'userlist': userlist
            }
        )

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.room_name
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
            'last_three': event.get('last_three', []),
            'userlist': event.get('userlist', [])
        }))

    async def get_userlist(self):
        chatroomusers = await sync_to_async(ChatRoomUsers.objects.filter)(room__name=self.room_name)
        chatroomusers = await sync_to_async(chatroomusers.distinct)()
        chatroomusers = await sync_to_async(chatroomusers.values_list)('user__username', flat=True)
        print(await sync_to_async(list)(chatroomusers))
        return await sync_to_async(list)(chatroomusers)
    
    
    async def user_disconnect(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user-left',
            'username': event['username'],
            'userlist': event.get('userlist', [])
        }))
        