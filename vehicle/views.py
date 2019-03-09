from django.shortcuts import render
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
