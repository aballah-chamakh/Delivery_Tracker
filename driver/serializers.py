from rest_framework import serializers
from account.serializers import UserSerializer
# from order.models import Order
# from order.models import OrderSerializer
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    vehicle = serializers.SerializerMethodField('get_driver_vehicle')
    # orders_attached = serializers.SerializerMethod('get_all_orders')
    image = serializers.CharField(source='image.url')
    class Meta :
        model = Driver
        fields = ['id','username','vehicle','image']
    def get_driver_vehicle(self,driver_obj):
        if driver_obj.vehicle is not None :
            vehicle_obj = driver_obj.vehicle
            vehicle_info = {'vehicle_id':vehicle_obj.id,'vehicle_name':vehicle_obj.name,'coordinate':{'latitude':vehicle_obj.latitude,'longtitude':vehicle_obj.longitude}}
            return vehicle_info
        return None

    # def orders_attached(self,driver_obj):
    #     orders = Order.objects.filter(vehicle=drive_obj.car)
    #     serializer = OrderSerializer(orders,many=True)
    #     return serializer.data
