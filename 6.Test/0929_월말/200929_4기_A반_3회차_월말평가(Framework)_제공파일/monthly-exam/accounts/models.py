from django.db import models
from django.conf import settings

class Store(models.Model):
    location = models.CharField(max_length=20)
    phonenum = models.CharField(max_length=20, null=True)


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=CASCADE)
    productname = models.CharField(max_length=30, null=True)
    cost = models.IntegerField()
    price = models.IntegerField()
    expirydate = models.DateField()
    stock = models.IntegerField()