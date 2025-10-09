
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),

]