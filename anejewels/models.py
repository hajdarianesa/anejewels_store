from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/',null=True, blank=True)
     

    
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    total = models.FloatField(default=0.0)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class MyTransaction(models.Model):
    pass