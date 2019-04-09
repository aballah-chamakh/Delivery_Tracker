from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from DeliveryCompany.models import DeliveryCompany
from account.models import User
import json

class DriverDeliveryCompanyConsumer(AsyncJsonWebsocketConsumer) :

    async def websocket_connect(self,event):
        print(event)
        user_obj = self.scope['user']
        print(user_obj)
        await self.set_or_clear_user_channel_name(user_obj,'set')
        await self.accept()



    async def websocket_receive(self,event):
        # update the user to match the data base change
        await self.update_user_obj(self.scope['user'])
        user_obj = self.scope['user']
        print(user_obj.username)
        if user_obj.isdriver :
            coordinates = json.loads(event['text'])['coordinates']
            await self.set_vehicle_coordinates(user_obj.driver,coordinates)
            deliverycompany_channel_name = await self.get_delivery_company_channel_name(self.scope['user'])
            if deliverycompany_channel_name != '' :
                await self.channel_layer.send(deliverycompany_channel_name,{'type':'send.coordinates',
                                                                           'coordinates':coordinates,
                                                                           'driver_id':user_obj.driver.id})
            else :
                print('delivery company not connected')
    async def websocket_disconnect(self,event):
        user_obj = self.scope['user']
        await self.set_or_clear_user_channel_name(user_obj,'clear')


    async def send_coordinates(self,event):
        coordinates = event['coordinates']
        driver_id = event['driver_id']
        print(coordinates)
        data = {'coordinates':coordinates,'driver_id':driver_id}
        await self.send_json(content=data)

    @database_sync_to_async
    def set_or_clear_user_channel_name(self,user_obj,action):
        if user_obj.isdeliverycompany :
            deliverycompany_obj = user_obj.deliverycompany
            if action == 'clear' :
                deliverycompany_obj.channel_name = ''
                print(deliverycompany_obj.company_name+' delivery_company is offline now')
            elif action == 'set' :
                deliverycompany_obj.channel_name = self.channel_name
                print(deliverycompany_obj.company_name+' delivery_company is online now')
            deliverycompany_obj.save()
            self.deliverycompany_obj = deliverycompany_obj
        elif user_obj.isdriver :
            driver_obj = user_obj.driver
            if action == 'clear' :
                driver_obj.channel_name = ''
                print(driver_obj.user.username+' driver is offline now')
            elif action == 'set' :
                driver_obj.channel_name = self.channel_name
                print(driver_obj.user.username+' driver is online now')
            driver_obj.save()
            self.driver_obj = driver_obj



    @database_sync_to_async
    def get_delivery_company_channel_name(self,user_driver_obj):
        driver_obj = user_driver_obj.driver
        return driver_obj.delivery_company.channel_name

    @database_sync_to_async
    def update_user_obj(self,user_obj):
        new_user_obj = User.objects.get(id=user_obj.id)
        self.scope['user'] = new_user_obj
        print('user updated')

    @database_sync_to_async
    def set_vehicle_coordinates(self,driver_obj,coordinates):
        vehicle_obj = driver_obj.vehicle
        vehicle_obj.latitude = coordinates[0]
        vehicle_obj.longtitude = coordinates[1]
        vehicle_obj.save()
