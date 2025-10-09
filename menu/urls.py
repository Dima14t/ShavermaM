from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),


    path('add_to_cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
]
