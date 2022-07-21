from django.db import models

from home.models import City


class Hotel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/hotels')
    description = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    price = models.PositiveBigIntegerField(default=1)

    @staticmethod
    def get_all_hotel():
        return Hotel.objects.all()


    def __str__(self):
        return self.title

    @staticmethod
    def get_all_hotel_by_city_id(city_id):
        if city_id:

            return Hotel.objects.filter(city=city_id)
        else:
            return Hotel.get_all_hotel();


