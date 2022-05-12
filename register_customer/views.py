import uuid

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token


# TODO : tokenize!
@api_view(["POST"])
def Register_customer(request):
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
            #    token = Token.objects.get_or_create(user=account)
            token = uuid.uuid4().hex
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data)
