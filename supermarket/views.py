from django.shortcuts import render
from . import models, serializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

import datetime


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
            inventory = self.request.query_params['inventory']
            description = self.request.query_params['description']
            expiration_date = self.request.query_params['expiration_date']
            production_date = self.request.query_params['production_date']
        elif self.request.data:
            title = self.request.data['title']
            first_price = self.request.data['first_price']
            final_price = self.request.data['final_price']
            inventory = self.request.data['inventory']
            description = self.request.data['description']
            expiration_date = self.request.data['expiration_date']
            production_date = self.request.data['production_date']
        else:
            message = "No data"
            return Response({'message': 'message'}, status = 400)

        if not (title and final_price and first_price and inventory and description and expiration_date and production_date):
            message = "Not enough data"
            return Response({'message': 'message'}, status = 400)


        expire = datetime.date(int(expiration_date[0:4]), int(expiration_date[4:6]), int(expiration_date[6:8]))
        product = datetime.date(int(production_date[0:4]), int(production_date[4:6]), int(production_date[6:8]))

        # expire = datetime.date(expiration_date['year'], expiration_date['month'], expiration_date['day'])
        # product = datetime.date(production_date['year'], production_date['month'], production_date['day'])


        # try:
        #     file = self.request.data['file']
        #     if not file:
        #         file = self.request.query_params['files']
        # except KeyError:
        #     message = "Request has no resource file attached"
        #     return Response({'message': 'message'}, status = 400)
        #     raise ParseError('Request has no resource file attached')


        product = models.Product(title = title, first_price = first_price, final_price = final_price,
                                inventory = inventory, description = description,
                                supermarket_user = self.request.user, expiration_date = expire, production_date = product,
                        )

        product.save()

        message = "The product was added successfully"
        return Response({'message': message, 'id': product.id}, status = 200)

    def get(self, *args, **kwargs):
        return Response()



class AddImage(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        p_id = int(self.kwargs['produt_id'])
        if not cat_id:
            message = "No Data"
            return Response({'message': 'message'}, status = 400)

        product = models.Product.objects.filter(id = p_id)
        if not product:
            message = "Not validdData"
            return Response({'message': 'message'}, status = 400)

        produt = product[0]

        try:
            file = self.request.data['file']
            if not file:
                file = self.request.query_params['files']
        except KeyError:
            message = "Request has no resource file attached"
            return Response({'message': 'message'}, status = 400)
            raise ParseError('Request has no resource file attached')

        product.image = file
        product.save()

        message = "The product Image was added successfully"
        return Response({'message': message, 'id': product.id}, status = 200)

    def get(self, *args, **kwargs):
        return Response()

class ListCategory(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
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


class ListProduct(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
            expiration_year = p.expiration_date.year
            expiration_month = p.expiration_date.month
            expiration_day = p.expiration_date.day

            production_year = p.production_date.year
            production_month = p.production_date.month
            production_day = p.production_date.day

            expire = str(expiration_year)
            if expiration_month < 10:
                expire += "0"
            expire += str(expiration_month)
            if expiration_day < 10:
                expire += "0"
            expire += str(expiration_day)

            product = str(product_year)
            if product_month < 10:
                product += "0"
            product += str(product_month)
            if product_day < 10:
                product += "0"
            product += str(products_day)

            item = {
                'id': p.id,
                'title': p.title,
                'first_price': p.first_price,
                'final_price': p.final_price,
                'discount': p.get_discount(),
                'description': p.description,
                # 'expiration_date': {
                #     'year': expiration_year,
                #     'month': expiration_month,
                #     'day': expiration_day
                # },
                # 'production_date': {
                #     'year': production_year,
                #     'month': production_month,
                #     'day': production_day
                # },
                'expiration_date': expire,
                'production_date': product,
                'image': p.image.url,
                'category': {
                    'title': p.category.title,
                    'id': p.category.id,
                }
            }
            data.append(item)

        message = "Product list"
        return Response({'message': message, 'products': data}, status = 200)




class DetailProduct(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        p_id = int(self.kwargs['product_id'])
        products = models.Product.filter(id = p_id)

        if not produts:
            message = "Product Id is not valid"
            return Response({'message': message,}, status = 400)
        p = products[0]

        expiration_year = p.expiration_date.year
        expiration_month = p.expiration_date.month
        expiration_day = p.expiration_date.day

        production_year = p.production_date.year
        production_month = p.production_date.month
        production_day = p.production_date.day

        expire = str(expiration_year)
        if expiration_month < 10:
            expire += "0"
        expire += str(expiration_month)
        if expiration_day < 10:
            expire += "0"
        expire += str(expiration_day)

        product = str(product_year)
        if product_month < 10:
            product += "0"
        product += str(product_month)
        if product_day < 10:
            product += "0"
        product += str(products_day)

        item = {
                'id': p.id,
                'title': p.title,
                'first_price': p.first_price,
                'final_price': p.final_price,
                'discount': p.get_discount(),
                'description': p.description,
                # 'expiration_date': {
                #     'year': expiration_year,
                #     'month': expiration_month,
                #     'day': expiration_day
                # },
                # 'production_date': {
                #     'year': production_year,
                #     'month': production_month,
                #     'day': production_day
                # },
                'expiration_date': expire,
                'production_date': product,
                'image': p.image.url,
                'category': {
                    'title': p.category.title,
                    'id': p.category.id,
                }
            }

        message = "Product Detail"
        return Response({'message': message, 'product': item}, status = 200)



class ListShop(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cat_id = int(self.kwargs['city'])

        shops = models.Shop.objects.filter(city = city)

        data = []

        for shop in shops:
            item = {
                'title': shop.title,
                'city': shop.city,
                'address': shop.address,
            }
            data.append(item)

        message = "Shop list"
        return Response({'message': message, 'shops': data}, status = 200)




#
