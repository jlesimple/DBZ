from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(default=0000.00)
    quantity=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    thumbnail=models.ImageField(upload_to="products", null=True, blank=True)
