from django.db import models
from DeliveryCompany.models import DeliveryCompany

class Vehicle(models.Model):
    delivery_company = models.ForeignKey(DeliveryCompany,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    latitue = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

    def __str__(self):
        return 'vehicle {name}'.format(name=self.name)
