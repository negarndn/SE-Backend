from rest_framework import serializers
from .models import Customer


class RegisterSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    password = serializers.CharField(required=False, min_length=4)

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
