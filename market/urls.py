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
from register_supermarket import views_S
from login_supermarket import views_S2
from register_supermarket.schema import schema
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerS/', views_S.Register_supermarket, name='registerS'),
    path('registerC/', views.Register_customer, name='registerC'),
    path('loginS/', views_S2.LoginSView.as_view(), name='registerC'),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
  #  path('', include('main.urls')),
]
