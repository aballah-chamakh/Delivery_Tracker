from django.shortcuts import render
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.viewsets import ModelViewSet
from driver.models import Driver
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self):
        qs = None
        if self.request.user and self.request.user.is_authenticated :
            qs = Vehicle.objects.filter(delivery_company=self.request.user.deliverycompany)
        return qs



    def perform_create(self,serializer):
        deliverycompany_obj = self.request.user.deliverycompany
        print(deliverycompany_obj)
        obj = serializer.save(delivery_company=deliverycompany_obj)
        obj.delivery_company = deliverycompany_obj
        obj.save()

    # def get_queryset(self):
    #     map = self.request.GET.get('map')
    #     if map is not None :
    #         qs = self.queryset.filter(tracked=True)
    #         return qs
    #     return self.queryset
    # @action(methods=['POST'],detail=False)
    # def create_vehicle(self, request):
    #     deliverycompany_obj = request.user.deliverycompany
    #     vehicle_name = request.data.get('vehicle_name')
    #     vehicle_img = request.data.get('img')
    #     driver_id = request.data.get('driver_id')
    #
    #     vehicle_obj = Vehicle.objects.create(delivery_company=deliverycompany_obj,
    #                                          name=vehicle_name)
    #     if vehicle_img :
    #         vehicle_obj.image = vehicle_img
    #         driver_obj.save()
    #     if driver_id :
    #         driver_obj = Driver.objects.get(id=driver_id)
    #         driver_obj.vehicle = vehicle_obj
    #         driver_obj.save()
    #     #serializer = VehicleSerializer(vehicle_obj,many=False)
    #     return Response({'vehicle_id':vehicle_obj.id},status=status.HTTP_200_OK)
    @action(methods=['PUT'],detail=True)
    def toogle_tracking(self,request,pk):
        vehicle_obj = self.get_object()
        vehicle_obj.tracked = request.data.get('tracked')
        vehicle_obj.save()
        return Response({'res':'tracking toogled'},status=status.HTTP_200_OK)
