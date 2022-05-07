from django.urls import path, include
from . import views


urlpatterns = [
    # path('product-list', views.product_list),
<<<<<<< HEAD
    path('get-product', views.ListProduct.as_view()),
=======
    path('get-category', views.ListCategory.as_view()),
    path('get-product/<int:cat_id>/', views.ListProduct.as_view()),
>>>>>>> 6c0390487d9d704aece46e24d17518410ca8b7d9
    path('add-product', views.AddProduct.as_view())
]
