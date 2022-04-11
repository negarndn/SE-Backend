from turtle import mode
from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, blank=False)
    address = models.TextField()
    blance = models.PositiveIntegerField(default=20000, null=True)
    city = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
