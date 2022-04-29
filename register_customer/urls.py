from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.Register_Users, name="register"),
]
