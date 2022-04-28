from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from rest_framework import generics
from .models import Customer
from .serializers import RegisterSerializer


class RegisterAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = RegisterSerializer

    # def post(self, request):


def register_customer(request):
    if request.method == 'GET':
        return render(request, template_name='main/register.html')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')  # urlname
