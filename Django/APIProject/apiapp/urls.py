from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path("", views.stdata),
    path("getalldata/", views.getalldata),
    path("getstid/<int:id>", views.getstid),
    path("deletestid/<int:id>", views.deletestid),
    path("savedata/", views.savedata),
    path("updatedata/<int:id>", views.updatedata),
]
