from django.shortcuts import render
from . import models, serializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.


# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'template_name', {'products': products})


class AddProduct(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        if self.request.query_params:
            title = self.request.query_params['title']
            first_price = self.request.query_params['first_price']
            final_price = self.request.query_params['final_price']
            discount = self.request.query_params['discount']
            inventory = self.request.query_params['inventory']
            comments = self.request.query_params['comments']
        elif self.request.data:
            title = self.request.data['title']
            first_price = self.request.data['first_price']
            final_price = self.request.data['final_price']
            discount = self.request.data['discount']
            inventory = self.request.data['inventory']
            comments = self.request.data['comments']
        else:
            message = "No data"
            return Response({'message': 'message'}, status = 400)

        if not (title and final_price and first_price and inventory and comments):
            message = "Not enough data"
            return Response({'message': 'message'}, status = 400)


        product = models.Product(title = title, first_price = first_price, final_price = final_price,
                                discount = discount, inventory = inventory, comments = comments,
                                supermarket_user = self.request.user
                        )
        product.save()

        message = "The product was added successfully"
        return Response({'message': message}, status = 200)

    def get(self, *args, **kwargs):
        return Response()






class ListProduct(APIView):
    def get(self, request, format=None):
        data = []
        products = models.Product.objects.all()

        for p in products:
            item = {
                'title': p.title,
                'first_price': p.first_price,
                'final_price': p.final_price,
                'discount': p.discount,
                'inventory': p.inventory,
                'comments': p.comments
            }
            data.append(item)

        message = "Product list"
        return Response({'message': message, 'products': data}, status = 200)








#
