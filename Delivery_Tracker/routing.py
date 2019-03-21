from django.conf.urls import url
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .tokenmiddlware import TokenAuthMiddlewareStack
from driver.consumers import DriverDeliveryCompanyConsumer
application = ProtocolTypeRouter({

    "websocket": TokenAuthMiddlewareStack(
        URLRouter([

            # path('ws/robot/<int:pk>/', RobotConsumer),
             path('ws/driver_delivery_company/',DriverDeliveryCompanyConsumer)
        ])
    ),

})
