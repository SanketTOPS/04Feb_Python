from django.db import models


# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=50)

    def __str__(self):
        return self.pname


class Product_detail(models.Model):
    pname = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    qty = models.IntegerField()
    pimage = models.ImageField(upload_to="media/MyProduct")
