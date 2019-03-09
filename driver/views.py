from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Driver
from .serializers import DriverSerializer
# Create your views here.


class DriverViewset(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
