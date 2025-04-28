from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    pdata=Product_detail.objects.all()
    return render(request, "index.html",{'pdata':pdata})
