from django.db import models


class OrderProduct(models.Model):
    order = models.ForeignKey('shopapp.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('shopapp.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order.created_at}-{self.product.name}'
