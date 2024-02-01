from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.fullname}'s Order for {self.product.name}"