from django import forms
from .models import *


class UsersignupForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = "__all__"


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = [
            "firstname",
            "lastname",
            "username",
            "password",
            "city",
            "state",
            "mobile",
        ]


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title", "desc", "notefile"]
