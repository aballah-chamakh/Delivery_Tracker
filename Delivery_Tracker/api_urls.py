from django.conf.urls import include
from djanfo.urls import path
from driver import urls as driver_urls
from vehicle import urls as vehicle_urls
from DeliveryCompany import urls as delivery_company_urls
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token


urlpatterns = [
path('',include(driver_urls)),
path('',include(vehicle_urls)),
path('',include(delivery_company_urls)),
path('token/', obtain_jwt_token, name='token_obtain_pair'),
path('token/refresh', refresh_jwt_token, name='token_refresh'),
]
