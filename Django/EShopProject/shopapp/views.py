from django.shortcuts import render
from .models import *
from .forms import *



# Create your views here.
def index(request):
    pdata=Product_detail.objects.all()
    return render(request, "index.html",{'pdata':pdata})


def addproduct(request):
    pname=Product.objects.all()
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Product added!")
        else:
            print(form.errors)
    return render(request,'addproduct.html',{'pname':pname})
