from django.db import models


class ProductInBasket(models.Model):
    product = models.ForeignKey('shopapp.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product.name}({self.quantity})'

    def total_price(self):
        return self.quantity * self.product.price
