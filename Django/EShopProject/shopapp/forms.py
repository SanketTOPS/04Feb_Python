from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product_detail
        fields=['pname','qty','price','pimage']