from rest_framework import serializers
from .models import Customer


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
