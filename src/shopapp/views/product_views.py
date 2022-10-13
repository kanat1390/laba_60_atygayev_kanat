from django.shortcuts import render
from django.views.generic import ListView, DetailView
from shopapp.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shopapp/product/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shopapp/product/product_detail.html'

