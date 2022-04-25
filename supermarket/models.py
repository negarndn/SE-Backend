from turtle import mode
from django.db import models
from django.contrib.auth.models import User

#test2

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, blank=False)
    address = models.TextField()
    balance = models.PositiveIntegerField(default=20000, null=True)
    city = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, )


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True)
    first_price = models.PositiveIntegerField()
    final_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True)
    expiration = models.DateField()
    inventory = models.IntegerField()
    comments = models.TextField()
