from django.shortcuts import render
from . import models, serializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
<<<<<<< HEAD
# Create your views here.
=======
>>>>>>> 6c0390487d9d704aece46e24d17518410ca8b7d9

import datetime

<<<<<<< HEAD
=======

>>>>>>> 6c0390487d9d704aece46e24d17518410ca8b7d9
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
<<<<<<< HEAD
            comments = self.request.query_params['comments']
=======
            description = self.request.query_params['description']
            expiration_date = self.request.query_params['expiration_date'] # YYYY,MM,DD
>>>>>>> 6c0390487d9d704aece46e24d17518410ca8b7d9
        elif self.request.data:
            title = self.request.data['title']
            first_price = self.request.data['first_price']
            final_price = self.request.data['final_price']
            discount = self.request.data['discount']
            inventory = self.request.data['inventory']
<<<<<<< HEAD
            comments = self.request.data['comments']
=======
            description = self.request.data['description']
            expiration_date = self.request.data['expiration_date']
>>>>>>> 6c0390487d9d704aece46e24d17518410ca8b7d9
        else:
            message = "No data"
            return Response({'message': 'message'}, status = 400)

<<<<<<< HEAD
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
=======
        if not (title and final_price and first_price and inventory and description and expiration_date):
            message = "Not enough data"
            return Response({'message': 'message'}, status = 400)

        expiration_date = expiration_date.split(',')
        expiration_date = datetime.date(int(expiration_date[0]), int(expiration_date[1]), int(expiration_date[2]))

        try:
            file = self.request.data['file']
            if not file:
                file = self.request.query_params['files']
        except KeyError:
            message = "Request has no resource file attached"
            return Response({'message': 'message'}, status = 400)
            raise ParseError('Request has no resource file attached')


        product = models.Product(title = title, first_price = first_price, final_price = final_price,
                                discount = discount, inventory = inventory, description = description,
                                supermarket_user = self.request.user, expiration_date = expiration_date,
                                image = file,
                        )

        product.save()

        message = "The product was added successfully"
        return Response({'message': message, 'id': product.id}, status = 200)
>>>>>>> 6c0390487d9d704aece46e24d17518410ca8b7d9

    def get(self, *args, **kwargs):
        return Response()



<<<<<<< HEAD



class ListProduct(APIView):
    def get(self, request, format=None):
        data = []
        products = models.Product.objects.all()

        for p in products:
            item = {
=======
class ListCategory(APIView):
    def get(self, request, format=None):
        data = []
        cats = models.Category.objects.all()

        for p in cats:
            item = {
                'title': p.category.title,
                'id': p.category.id,
                }
            data.append(item)

        message = "Category list"
        return Response({'message': message, 'categories': data}, status = 200)


def cat_is_valid(cat_id):
    cat = models.Category.objects.filter(id = cat_id)
    if cat:
        return True
    return False

class ListProduct(APIView):
    def get(self, request, format=None):
        cat_id = int(self.kwargs['cat_id'])
        data = []
        products = models.Product.objects.all()

        if cat_id >= 1:
            if cat_is_valid(cat_id):
                products = products.filter(category__id = cat_id)
            else:
                message = "Category Id is not valid"
                return Response({'message': message,}, status = 400)

        for p in products:
            item = {
                'id': p.id,
>>>>>>> 6c0390487d9d704aece46e24d17518410ca8b7d9
                'title': p.title,
                'first_price': p.first_price,
                'final_price': p.final_price,
                'discount': p.discount,
                'inventory': p.inventory,
<<<<<<< HEAD
                'comments': p.comments
=======
                'description': p.description,
                'expiration_date': str(p.expiration_date),
                'image': p.image.url,
                'category': {
                    'title': p.category.title,
                    'id': p.category.id,
                }
>>>>>>> 6c0390487d9d704aece46e24d17518410ca8b7d9
            }
            data.append(item)

        message = "Product list"
        return Response({'message': message, 'products': data}, status = 200)








#
