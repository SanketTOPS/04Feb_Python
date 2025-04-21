from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def index(request):
    if request.method == "POST":
        unm = request.POST.get("username")
        pas = request.POST.get("password")
        user = usersignup.objects.filter(username=unm, password=pas)
        if user:
            print("Login Successfull!")
            return redirect("home")
        else:
            print("Error!Login faild...")
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfully!")
            return redirect("/")
        else:
            print(form.errors)
    return render(request, "signup.html")


def home(request):
    return render(request, "home.html")
