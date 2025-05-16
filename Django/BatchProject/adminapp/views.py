from django.shortcuts import render, redirect, get_object_or_404
from noteapp.models import *
from datetime import datetime

# Create your views here.


def adminlogin(request):
    if request.method == "POST":
        unm = request.POST["username"]
        pas = request.POST["password"]

        if unm == "admin" and pas == "admin@123":
            print("Login Successfull!")
            return redirect("adminhome")
        else:
            print("Error! Invalid Username or Password...")
    return render(request, "adminlogin.html")


def adminhome(request):
    return render(request, "adminhome.html")


def admin_alluser(request):
    alluser = Usersignup.objects.all()
    return render(request, "admin_alluser.html", {"alluser": alluser})


def admin_allnotes(request):
    allnotes = Notes.objects.all()
    return render(request, "admin_allnotes.html", {"allnotes": allnotes})


def approve_note(request, id):
    note = get_object_or_404(Notes, id=id)
    note.status = "Approved"
    note.updated_at = datetime.now()
    note.save()
    print("Your notes has been approved!")
    return redirect("admin_allnotes")


def reject_note(request, id):
    note = get_object_or_404(Notes, id=id)
    note.status = "Rejected"
    note.updated_at = datetime.now()
    note.save()
    print("Your notes has been rejected!")
    return redirect("admin_allnotes")
