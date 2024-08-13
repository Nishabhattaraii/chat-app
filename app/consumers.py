from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self):
        print("channel layer ....",self.channel_layer)#to get default channel layer from project
        async_to_sync (self.channel_layer.group_add)('programmers',self.channel_name) 
        self.send({
            'type':'websocket.accept'
        })

    def websocket_disconnect(self, event):
        print('websocket disconnected...',event)
        print("channel layer ....",self.channel_layer)
        async_to_sync(self.channel_layer.group_discard)('programmers',self.channel_name)
        raise StopConsumer


    def websocket_receive(self, event):
        async_to_sync( self.channel_layer.group_send)('programmers',{
            'type': 'chat.message',
            'message':event['text']
        })
        
    def chat_message(self,event):
        print('Event ...',event)
        print('Actual Data ...',event['message'])
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })