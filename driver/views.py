from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from account.serializers import UserSerializer
from vehicle.models import Vehicle
# Create your views here.


class DriverViewset(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    # def get_queryset(self):
    #     # if self.request.user :
    #     #     return self.queryset.filter(delivery_company=self.request.user.deliverycompany)
    #     return self.queryset
    def get_queryset(self):
        map = self.request.GET.get('map')
        qs = None
        print(self.request.user)
        if self.request.user and self.request.user.is_authenticated :
            qs = Driver.objects.filter(delivery_company=self.request.user.deliverycompany)
            if map :
                qs =  qs.filter(vehicle__tracked=True)
                print(qs)

        return qs
    @action(methods=['POST'],detail=False)
    def create_user_driver(self,request):
        email = request.data.get('email')
        username = request.data.get('username')
        pw1 = request.data.get('password')
        pw2 = request.data.get('password2')
        vehicle_id = request.data.get('vehicle_id')
        img = request.data.get('img')
        data = {'email':email,'username':username,'password':pw1,'password2':pw2}
        serializer = UserSerializer(data=data)
        user_obj = None
        if serializer.is_valid() :
            user_obj = serializer.save()
        else :
            return Response({'res':'user not valid'},status=status.HTTP_400_BAD_REQUEST)
        deliverycompany_obj = request.user.deliverycompany
        driver_obj = Driver.objects.create(user=user_obj,delivery_company=deliverycompany_obj)
        if vehicle_id is not None  :
            print(vehicle_id)
            vehicle_obj = Vehicle.objects.get(id=int(vehicle_id))
            if hasattr(vehicle_obj,'driver') :
                old_driver_obj = vehicle_obj.driver
                old_driver_obj.vehicle = None
                old_driver_obj.save()
            driver_obj.vehicle = vehicle_obj
            driver_obj.save()
        if img is not None :
            print('img is not None')
            driver_obj.image = img
            driver_obj.save()
        return Response({'driver_id':driver_obj.id},status=status.HTTP_200_OK)
