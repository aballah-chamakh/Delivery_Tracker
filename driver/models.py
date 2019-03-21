from django.db import models
from account.models import User
from vehicle.models import Vehicle
from DeliveryCompany.models import DeliveryCompany


class Driver(models.Model):
    user     = models.OneToOneField(User,on_delete=models.CASCADE)
    image    = models.ImageField(default='driver_img.jpg')
    vehicle  = models.OneToOneField(Vehicle,on_delete=models.SET_NULL,null=True,blank=True)
    delivery_company = models.ForeignKey(DeliveryCompany,on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        if self.vehicle :
            return 'the driver {username} work at {deliverycompany} and currently driver {vehicle}'.format(username=self.user.username,
                                                                                                           deliverycompany=self.delivery_company.company_name,
                                                                                                           vehicle=self.vehicle.name )
        return 'the driver {username} work at {deliverycompany} and currently driver nothing'.format(username=self.user.username,
                                                                                                      deliverycompany=self.delivery_company.company_name,
                                                                                                       )
