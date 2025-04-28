from django.contrib import admin
from .models import *

# Register your models here.


class Product_data(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "pname", "qty", "price", "pimage"]


admin.site.register(Product)
admin.site.register(Product_detail, Product_data)
