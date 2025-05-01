from django.contrib import admin
from django.urls import path, include
from shopapp import views

urlpatterns = [
    path("", views.index),
    path("addproduct/",views.addproduct),
]
