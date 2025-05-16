from django.contrib import admin
from django.urls import path, include
from adminapp import views

urlpatterns = [
    path("", views.adminlogin),
    path("adminhome/", views.adminhome, name="adminhome"),
    path("admin_alluser/", views.admin_alluser, name="admin_alluser"),
    path("admin_allnotes/", views.admin_allnotes, name="admin_allnotes"),
    path("approve_note/<int:id>", views.approve_note, name="approve_note"),
    path("reject_note/<int:id>", views.reject_note, name="reject_note"),
]
