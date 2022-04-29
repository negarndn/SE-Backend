from django.contrib.auth import authenticate
from rest_framework import serializers

from register_supermarket.models import Supermarket


class LoginSerializersS(serializers.Serializer):
    class Meta:
        model = Supermarket
        national_num_sup = serializers.CharField(max_length=255)
        password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email and password:

            user = authenticate(username=email, password=password)
            if user:
                data['user'] = user

            data['user'] = user
        return data
