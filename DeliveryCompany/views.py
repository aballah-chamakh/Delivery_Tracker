from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import DeliveryCompany
from .serializers import DeliveryCompanySerializer
# from driver.models import Driver
from driver.serializers import DriverSerializer
from vehicle.serializers import VehicleSerializer

class DeliveryCompanyViewset(ModelViewSet):
    queryset = DeliveryCompany.objects.all()
    serializer_class = DeliveryCompanySerializer
    @action(methods=['post'],detail=True)
    def create_new_driver(self,request,pk):
        driver = json.load(requets.data.get('driver'))
        serializer = UserSerializer(data=driver)
        if serializer.is_valid() :
            user_obj = serializer.save()
            driver_obj = Driver.objects.create(user=user_obj)
            driver_serializer = DriverSerializer(driver_obj,many=False)
            return Response({'response':'new driver was added successfully','driver':driver_serializer.data},status=status.HTTP_200_OK)
        return Response({'response':'not valid data'},status=status.HTTP_400_BAD_REQUEST)
    @action(methods=['POST'],detail=True)
    def create_new_vehicle(self,requet,pk):
        vehicle = json.load(requets.data.get('vehicle'))
        serializer = VehicleSerializer(data)
        if serializer.is_valid() :
            serializer.save()
            return Response({'response':'new vehicle was added successfully','driver':serializer.data},status=status.HTTP_200_OK)
        return Response({'response':'not valid data'},status=status.HTTP_400_BAD_REQUEST)
