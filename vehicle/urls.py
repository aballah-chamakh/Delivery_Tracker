from rest_framework import routers
from .views import VehicleViewSet
from django.conf.urls import  include
from django.urls import path

router = routers.DefaultRouter()
router.register('vehicle',VehicleViewSet)

urlpatterns = [
path('',include(router.urls)),
]
