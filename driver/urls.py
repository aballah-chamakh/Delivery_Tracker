from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import DriverViewset

router = routers.DefaultRouter()
router.register('driver',DriverViewset)
urlpatterns = [
path('',include(router.urls))
]
