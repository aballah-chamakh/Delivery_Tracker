from django.db import models
from DeliveryCompany.models import DeliveryCompany

class Vehicle(models.Model):

    delivery_company = models.ForeignKey(DeliveryCompany,on_delete=models.CASCADE,blank=True,null=True)
    image    = models.ImageField(default='vehicle_img.jpg')
    name = models.CharField(max_length=255,blank=True,null=True)
    latitude = models.CharField(max_length=255,default='0')
    longitude = models.CharField(max_length=255,default='0')
    tracked = models.BooleanField(default=False)

    def __str__(self):
        if self.image :
            return 'vehicle {name} with image {image}'.format(name=self.name,image=self.image.url)
        return 'vehicle {name}'.format(name=self.name)
