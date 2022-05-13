from django.urls import path, include
from . import views


urlpatterns = [
    # path('product-list', views.product_list),
    path('get-category', views.ListCategory.as_view()),
    path('get-product/<int:cat_id>/', views.ListProduct.as_view()),
    path('get-product-detail/<int:product_id>/', views.DetailProduct.as_view()),
    path('add-product', views.AddProduct.as_view()),
    path('add-product-image/<int:product_id>/', views.AddImage.as_view()),
    path('get-shop/<str:city>/', views.ListShop.as_view()),
]
