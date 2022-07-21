from django.contrib.auth.models import User
from  django.db import  models

from home.models import Hotel


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return  str(self.id)

