from django.db import models
from website.settings import AUTH_USER_MODEL

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0000.00)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    oredered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
