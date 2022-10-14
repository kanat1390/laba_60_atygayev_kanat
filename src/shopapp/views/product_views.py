from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from shopapp.forms import ProductForm
from shopapp.models import Product
from shopapp.mixins import SuccessDetailUrlMixin, ExtraContextMixin, SuccessListUrlMixin


class ProductListView(ListView):
    model = Product
    template_name = 'shopapp/product/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shopapp/product/product_detail.html'


class ProductCreateView(ExtraContextMixin, SuccessDetailUrlMixin, CreateView):
    model = Product
    template_name = 'shopapp/product/product_form.html'
    form_class = ProductForm
    success_url = 'product-detail'
    extra_context = {
        'form_title': 'Создать продукт',
    }


class ProductUpdateView(ExtraContextMixin, SuccessDetailUrlMixin, UpdateView):
    model = Product
    template_name = 'shopapp/product/product_form.html'
    form_class = ProductForm
    success_url = 'product-list'
    extra_context = {
        'form_title': 'Изменить продукт',
    }


class ProductDeleteView(SuccessListUrlMixin, DeleteView):
    model = Product
    success_url = 'product-list'
    template_name = 'shopapp/product/product_confirm_delete.html'
