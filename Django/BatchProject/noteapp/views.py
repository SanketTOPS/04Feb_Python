from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.mail import send_mail
import random
from BatchProject import settings
from django.contrib.auth import logout
from datetime import datetime


# Create your views here.
def index(request):
    user = request.session.get("user")
    return render(request, "index.html", {"user": user})


def notes(request):
    user = request.session.get("user")
    username = Usersignup.objects.get(username=user)
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            cuser = form.save(commit=False)
            cuser.status = "Pending"
            cuser.username = username
            cuser.save()
            print("Your Notes has been submitted!")
        else:
            print(form.errors)
    return render(request, "notes.html", {"user": user})


def profile(request):
    msg = ""
    user = request.session.get("user")
    userid = request.session.get("userid")
    cuser = Usersignup.objects.get(id=userid)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=cuser)
        if form.is_valid():
            form.save()
            print("Profile updated!")
            return redirect("profile")
        else:
            print(form.errors)
            msg = "Error! Something went wrong..."
    return render(request, "profile.html", {"user": user, "cuser": cuser, "msg": msg})


def about(request):
    user = request.session.get("user")
    return render(request, "about.html", {"user": user})


def contact(request):
    user = request.session.get("user")
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Your inquery has been submitted! ")
            return redirect("contact")
        else:
            print(form.errors)
    return render(request, "contact.html", {"user": user})


def login(request):
    user = request.session.get("user")
    msg = ""
    if request.method == "POST":
        unm = request.POST["username"]
        pas = request.POST["password"]

        user = Usersignup.objects.filter(username=unm, password=pas)
        userid = Usersignup.objects.get(username=unm)
        print("Userid:", userid.id)
        if user:
            print("Login Successfull!")
            request.session["user"] = unm
            request.session["userid"] = userid.id
            return redirect("notes")
        else:
            print("Error!Login faild...")
            msg = "Error!Login faild..."
    return render(request, "login.html", {"msg": msg, "user": user})


def signup(request):
    user = request.session.get("user")
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

            # Email Send Code
            global otp
            otp = random.randint(1111, 9999)
            sub = "Your OTP"
            msg = f"Dear User!\n\nThanks for signup\n\nYour one time password for verification is:{otp}.\n\nThanks & Regards\nNoteApp - Admin\nTOPS Technologies-Rajkot\n9724799469 | www.tops-int.com"
            from_email = settings.EMAIL_HOST_USER
            to_email = [request.POST["username"]]
            send_mail(
                subject=sub, message=msg, from_email=from_email, recipient_list=to_email
            )

            return redirect("otpverify")
    return render(request, "signup.html", {"msg": msg, "user": user})


def otpverify(request):
    user = request.session.get("user")
    print("OTP:", otp)
    msg = ""
    if request.method == "POST":
        if request.POST["otp"] == str(otp):
            print("Verification Success!")
            return redirect("login")
        else:
            print("Error! Verification faild...")
            msg = "Error! Verification faild..."
    return render(request, "otpverify.html", {"msg": msg, "user": user})


def userlogout(request):
    logout(request)
    return redirect("/")
