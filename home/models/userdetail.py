from django.contrib.auth.models import User
from django.db import models

from home.models import Hotel


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default='')
    first_name = models.CharField(max_length=75, null=True)
    last_name = models.CharField(max_length=75, null=True)
    quantity = models.PositiveBigIntegerField(default=1)
    email = models.EmailField(max_length=30, null=True)
    phone_number = models.BigIntegerField(default=0, null=True)
    date_reserve = models.DateTimeField(auto_now_add=True, null=True)
    notes = models.CharField(max_length=200, default='')
