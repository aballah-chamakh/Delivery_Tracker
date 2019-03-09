from django.db import models
from account.models import User
from vehicle.models import Vehicle
from DeliveryCompany.models import DeliveryCompany


class Driver(models.Model):
    user     = models.OneToOneField(User,on_delete=models.CASCADE)
    vehicle  = models.OneToOneField(Vehicle,on_delete=models.CASCADE)
    delivery_company = models.ForeignKey(DeliveryCompany,on_delete=models.CASCADE)
