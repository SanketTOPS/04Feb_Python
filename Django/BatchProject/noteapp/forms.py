from django import forms
from .models import *


class UsersignupForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = "__all__"
