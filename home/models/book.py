from django.contrib.auth.models import User
from  django.db import  models
from home.models import Hotel

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default="1")
    book_date = models.DateTimeField(auto_now_add=True)




