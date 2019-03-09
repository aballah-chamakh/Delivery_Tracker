from rest_framework import serializers
from vehicle.serilaizers import VehicleSerializer
from vehicle.models import Vehicle
from driver.serializers import DriverSerializer
from driver.models import Driver

class DeliveryCompanySerializer(serializers.ModelSerializer):
    company_owner = serilaizers.CharField(source='user.username')
    vehicles = serializers.SerializerMethodField('get_all_company_vehicles')
    drivers = serializers.SerializerMethodField('get_all_company_drivers')
    class Meta :
        fields = ['company_name','vehicles','drivers']
    def get_all_company_vehicles(self,delivery_company_obj):
        qs_vehicles = Vehicle.objects.filter(delivery_company=delivery_company_obj)
        serializer = VehicleSerializer(qs_serializer,many=True)
        return serialiazer.data
    def get_all_company_drivers(self,delivery_company_obj):
        qs_drivers = Driver.objects.filter(delivery_company=delivery_company_obj)
        serializer = DriverSerializer(qs_drivers,many=True)
        return serializer.data
