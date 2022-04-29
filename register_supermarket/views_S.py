from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token


# TODO : tokenize!
@api_view(["POST"])
def Register_supermarket(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered"
            data['id_sup'] = account.id_sup
            data['name_sup'] = account.name_sup
            data['national_num_sup'] = account.national_num_sup
            data['password_sup'] = account.password_sup
        #    token = Token.objects.get_or_create(user=account)
        #    data['token'] = token
        else:
            data = serializer.errors

        return Response(data)
