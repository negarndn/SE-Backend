"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from register_customer import views
from register_customer.views import RegisterAPIViewC
from register_supermarket.views import RegisterAPIViewS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerS/', RegisterAPIViewS.as_view(), name='registerS'),
    path('registerC/', views.Register_Users, name='registerC'),
    path('loginC/', RegisterAPIViewC.as_view(), name='register2'),
    path('', include('main.urls')),
]
