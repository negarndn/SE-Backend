from django.urls import path, include
from . import views


urlpatterns = [
    # path('product-list', views.product_list),
    path('get-product', views.ListProduct.as_view()),
    path('add-product', views.AddProduct.as_view())
]
