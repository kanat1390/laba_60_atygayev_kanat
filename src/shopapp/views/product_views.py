from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)

from searchview.views import SearchView

from shopapp.forms import ProductForm
from shopapp.models import Product, ProductInBasket
from shopapp.mixins import SuccessDetailUrlMixin, ExtraContextMixin, SuccessListUrlMixin
from shopapp.forms import ProductSearchForm


class ProductListView(SearchView):
    model = Product
    template_name = 'shopapp/product/product_list.html'
    form_class = ProductSearchForm
    first_display_all_list = True
    paginate_by = 10
    ordering = ['name', 'category__name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        basket_list = ProductInBasket.objects.all()
        context.update({
            'basket_list': basket_list,
            'basket_qty': len(basket_list),
        })
        return context


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
