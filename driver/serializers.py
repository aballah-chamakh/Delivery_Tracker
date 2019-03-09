from rest_framework import serializers
from account.serializers import UserSerializer
from order.models import Order
from order.models import OrderSerializer


class DriverSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    vehicle = serializers.CharField(source='vehicle.name')
    orders_attached = serializers.SerializerMethod('get_all_orders')
    class Meta :
        fields = ['user','vehicle','orders_attached']

    def orders_attached(self,driver_obj):
        orders = Order.objects.filter(vehicle=drive_obj.car)
        serializer = OrderSerializer(orders,many=True)
        return serializer.data
