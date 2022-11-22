from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30, null=True,blank=True)
    price = models.CharField(max_length=40,null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)