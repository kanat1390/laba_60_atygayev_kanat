from email.policy import default
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, max_length=2000, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, upload_to='shopapp/images', verbose_name='Изображение')
    category = models.ForeignKey('shopapp.Category', on_delete=models.CASCADE, verbose_name='Категория')
    in_stock = models.IntegerField(verbose_name='Количество в наличии')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name

