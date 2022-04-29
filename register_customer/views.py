from sqlite3 import IntegrityError
#from tokenize import Token
from tokenize import Token

from django.shortcuts import redirect
from rest_framework import generics
#from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Customer
from .serializers import RegisterSerializer


class RegisterAPIViewC(generics.ListCreateAPIView):
    # get method handler
    queryset = Customer.objects.all()
    serializer_class = RegisterSerializer


@api_view()
@permission_classes([AllowAny])
def Register_Users(request):
    try:
        data = []
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            account.save()
            token = Token.objects.get_or_create(user=account)[0].key
            data["message"] = "user registered successfully"
            data["first name"] = account.first_name
            data["last name"] = account.last_name
            data["phone"] = account.phone
            data["city"] = account.city
            data["address"] = account.adress
            data["password"] = account.password
            data["token"] = token

        else:
            data = serializer.errors

        return Response(data)
    except IntegrityError as e:
        account = Customer.objects.get(username='')
        account.delete()
        raise ValidationError({"400": f'{str(e)}'})

    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})
