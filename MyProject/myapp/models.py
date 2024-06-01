from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    dedescription = models.TextField()
    price= models.DecimalField(max_digits=4, decimal_places=2)
    stock= models.IntegerField()
    image = models.ImageField(upload_to='images/')

class Order(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(
        Product,
        through="ItemOrder",
        through_fields=("order", "product"),
    )

class ItemOrder(models.Model):
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    