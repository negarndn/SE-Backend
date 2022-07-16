from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from rest_framework.authtoken.models import Token


# from django.contrib.auth.models import User

# model for database table
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, blank=False)
    address = models.TextField(blank=True)
    balance = models.PositiveIntegerField(default=20000, null=True)
    city = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.first_name)

    def deposit(self, amount: int):
        """ Charges user's balance by <amount> Tomans.
        :param amount:int
        :return:void
        """
        self.balance += amount
        pass

    def spent(self, amount: int):
        """ Decreases user's balance by <amount> Tomans.
        :param amount:int
        :return:void
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise Exception("Customer balance is not enough!")
        pass
