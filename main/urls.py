from django.urls import path
from main import views
from register_supermarket import views as register_view

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    # path('register/', register_view.RegisterAPIView, name='register'),

]
