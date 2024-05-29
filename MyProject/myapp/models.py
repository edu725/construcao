from django.db import models

# Create your models here.

class Produto(models.Model):
    name = models.CharField(max_length=200)
    dedescription = models.TextField()
    price= models.DecimalField(max_digits=4, decimal_places=2)
    stock= models.IntegerField()