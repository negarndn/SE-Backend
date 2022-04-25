from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def homepage(request):
    # return  HttpResponse('<h1>Hello</h1>')
    return render(request, template_name='main/home.html')


def loginpage(request):
    return render(request, template_name='main/login.html')


def registerpage(request):
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


def logoutpage(request):
    pass
