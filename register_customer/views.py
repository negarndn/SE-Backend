import uuid

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.authtoken.models import Token


# TODO : tokenize!
@api_view(["POST"])
def Register_customer2(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered"
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['phone'] = account.phone
            data['city'] = account.city
            data['address'] = account.address
            data['password'] = account.password
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors
        return Response(data)


@api_view(["POST"])
def Register_customer(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['message'] = 'Done!'
            data['token'] = Token.objects.get(user=user).key
            data["username"] = user.username
        return Response(data)
