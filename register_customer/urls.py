from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.RegisterAPIViewC.as_view(), name="register"),
]
