from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import DeliveryCompanyViewset

router = routers.DefaultRouter()
router.register('delivery_company',DeliveryCompanyViewset)

urlpatterns = [
path('',include(router.urls))
]
