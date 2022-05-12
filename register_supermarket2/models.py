from django.db import models
from django.contrib.auth.models import User


# model for database table
class Supermarket(models.Model):
    id_sup = models.IntegerField(primary_key=True)
    name_sup = models.CharField(max_length=20)
    national_num_sup = models.IntegerField()
    phone = models.CharField(max_length=11, min_lenght=11)
    password_sup = models.CharField(max_length=20, min_lenght=4)
    date_created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=250)
    address = models.TextField(blank=True)
    from_hour = models.TimeField(blank=True)
    to_hour = models.TimeField(blank=True)
    owner = models.TextField(max_length=250, blank=True)
    SMS_TEST = 1111
    SMS_CHOICES = (
        (SMS_TEST, '1111'),
    )
    sms = models.IntegerField(choices=SMS_CHOICES)
    # custom configs for super class

    class Meta:
        ordering = ['-date_created']  # order in serialized (json) file

    def __str__(self):
        return self.name_sup
