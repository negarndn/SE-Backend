from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'phone',
            'address',
            'city',
            'password',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
