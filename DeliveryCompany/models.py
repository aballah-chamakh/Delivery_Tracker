from django.db import models
from account import User


class DeliveryCompany(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    # some additional info
    def __str__(self):
        return 'delivery company owned by {username}'.format(username=self.user.username)
        
