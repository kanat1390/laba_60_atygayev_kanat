from email.policy import default
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=2000)
    image = models.ImageField(null=True, blank=True, upload_to='shopapp/images')
    category = models.ForeignKey('shopapp.Category', on_delete=models.CASCADE)
    in_stock = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

