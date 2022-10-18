from django.contrib import admin
from shopapp.models import Product, Category, ProductInBasket, Order, OrderProduct

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductInBasket)
admin.site.register(Order)
admin.site.register(OrderProduct)
