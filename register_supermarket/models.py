from django.db import models
from django.contrib.auth.models import User


# model for database table
class Supermarket(models.Model):
    id_sup = models.IntegerField(primary_key=True)
    name_sup = models.CharField(max_length=20)
    national_num_sup = models.IntegerField()
    password_sup = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    # custom configs for super class
    class Meta:
        ordering = ['-date_created']  # order in serialized (json) file

    def __str__(self):
        return self.name_sup
