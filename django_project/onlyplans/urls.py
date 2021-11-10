from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('friends/', views.my_friends),
]
