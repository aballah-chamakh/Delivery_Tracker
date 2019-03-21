from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
import json

class DriverDeliveryCompanyConsumer(AsyncJsonWebsocketConsumer) :

    async def websocket_connect(self,event):
        print(event)
        user_obj = self.scope['user']
        print(user_obj)
        await self.set_to_user_channel_name(user_obj)
        await self.accept()



    async def websocket_receive(self,event):
        if self.scope['user'].isdriver :
            coordinate = json.loads(event['text'])['coordinate']

            deliverycompany_channel_name = await self.get_delivery_company_channel_name(self.driver_obj)
            await self.channel_layer.send(deliverycompany_channel_name,{'type':'send.coordinate',
                                                                         'coordinate':coordinate})

    async def websocket_disconnect(self,event):
        print(event)


    async def send_coordinate(self,event):
        coordinate = event['coordinate']
        print(coordinate)
        data = {'coordinate':coordinate}
        await self.send_json(content=data)

    @database_sync_to_async
    def set_to_user_channel_name(self,user_obj):
        if user_obj.isdeliverycompany :
            deliverycompany_obj = user_obj.deliverycompany
            deliverycompany_obj.channel_name = self.channel_name
            deliverycompany_obj.save()
            print(deliverycompany_obj)
            self.deliverycompany_obj = deliverycompany_obj
        elif user_obj.isdriver :
            driver_obj = user_obj.driver
            driver_obj.channel_name = self.channel_name
            driver_obj.save()
            print(driver_obj)
            self.driver_obj = driver_obj

    @database_sync_to_async
    def get_delivery_company_channel_name(self,driver_obj):
        return driver_obj.delivery_company.channel_name
