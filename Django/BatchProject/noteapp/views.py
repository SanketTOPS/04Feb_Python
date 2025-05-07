from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def notes(request):
    return render(request, "notes.html")


def profile(request):
    return render(request, "profile.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    msg = ""
    if request.method == "POST":
        form = UsersignupForm(request.POST)
        username = ""
        try:
            if form.is_valid():
                username = Usersignup.objects.get(username=request.POST["username"])
                username = form.cleaned_data.get(username)
                print("Username is already exists!")
                msg = "Username is already exists!"
        except Usersignup.DoesNotExist:
            form.save()
            print("Signup Successfully!")
            return redirect("login")
    return render(request, "signup.html", {"msg": msg})
