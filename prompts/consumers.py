# prompts/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PromptConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Called when a WebSocket connection is established.
        # You can perform authentication or join groups here.
        self.room_name = 'prompts' # Example: join a generic 'prompts' group
        self.room_group_name = f'chat_{self.room_name}' # Channels group name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept() # Accept the WebSocket connection

    async def disconnect(self, close_code):
        # Called when a WebSocket connection is closed.
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # We won't implement receive or sending messages yet,
    # but this is where you would handle incoming WebSocket messages.
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # Receive message from room group
    # async def chat_message(self, event):
    #     message = event['message']
    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({
    #         'message': message
    #     }))
