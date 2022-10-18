from django.db import models


class Order(models.Model):
    products = models.ManyToManyField('shopapp.Product', related_name='orders')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.created_at}'
