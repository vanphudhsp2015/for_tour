from django.db import models
from datetime import datetime
from tourer.models import Tourer
from django.urls import reverse
# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    # def get_absolute_url(self):
    #     return reverse('IndexView_Place_City')

    def __str__(self):
        return self.city + '-' + self.address


class Restaurant(models.Model):
    name_restaurant = models.CharField(max_length=250)
    location = models.ForeignKey(City,on_delete=models.CASCADE)
    type_restaurant = models.CharField(max_length=250)
    image_restaurant = models.FileField(upload_to = 'restaurant/',default='/default/user-avatar-default-165.png')
    review = models.IntegerField(default=0)
    star = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('IndexView_Restaurants')

    def __str__(self):
        return self.name_restaurant + '-' + self.location.city

class Eating(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name_food = models.CharField(max_length=250)
    info_food = models.CharField(max_length=250)
    price = models.FloatField(default=0,null=True,blank=True)
    img_status = models.FileField(upload_to='restaurant/book/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('IndexView_Eating')

    def __str__(self):
        return self.restaurant.name_restaurant + '-' + self.name_food

class Eating_details(models.Model):
    eating = models.ForeignKey(Eating,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    start_status = models.CharField(max_length=5000)
    end_status = models.CharField(max_length=5000)
    img_status = models.FileField(upload_to='house/book/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('IndexView_Eating_details')

    def __str__(self):
        return self.eating.name_food + '-' + self.title

class Comment_restaurant(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    commnet = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)

