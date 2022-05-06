from django.db import models
from django.db import models
# from rest_framework.authtoken.admin import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# class Customer(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=11, blank=False)
#     address = models.TextField()
#     balance = models.PositiveIntegerField(default=20000, null=True)
#     city = models.CharField(max_length=255)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class UserProfileManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, password = None):
        user = self.model(username = username, first_name = first_name, last_name = last_name)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, username, first_name, last_name , password = None):

        user = self.create_user(username, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user


MODES = (
('customer', 'customer'),
('supermarket', 'supermarket'),
)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    username =  models.CharField(max_length = 255, unique = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    mode = models.CharField(max_length = 20, choices = MODES)

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField( default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
         verbose_name = 'User'
         verbose_name_plural = 'Users'
         ordering = ('-last_name',)


    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Category(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True)
    expiration_date = models.DateField()
    supermarket_user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    first_price = models.PositiveIntegerField()
    final_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True)
    inventory = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
