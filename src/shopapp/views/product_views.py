from django.shortcuts import render

from shopapp.models import Product
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView
    )


# class SuccessUrlMixin():


class ProductListView(ListView):
    model = Product
    template_name = 'shopapp/product/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shopapp/product/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'shopapp/product/product_form.html'
    fields = ('name', 'description', 'image', 'category', 'in_stock', 'price')



