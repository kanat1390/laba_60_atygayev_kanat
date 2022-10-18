from itertools import product
from unicodedata import name
from shopapp.models import ProductInBasket, Product, Order, OrderProduct
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from shopapp.forms import ContactForm


# def add_to_basket(request, pk):
#     baskets = ProductInBasket.objects.filter(product__id=pk)
#     if baskets:
#         basket = baskets[0]
#         if (basket.product.in_stock - (basket.quantity + 1)) >= 0:
#             basket.quantity += 1
#             basket.save()
#     else:
#         product = get_object_or_404(Product, pk=pk)
#         if product.in_stock > 0:
#             ProductInBasket.objects.create(product=product, quantity=1)

#     return redirect('product-list')


class ProductAddToBasket(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        baskets = ProductInBasket.objects.filter(product__id=pk)
        if baskets:
            basket = baskets[0]
            if (basket.product.in_stock - (basket.quantity + 1)) >= 0:
                basket.quantity += 1
                basket.save()
        else:
            product = get_object_or_404(Product, pk=pk)
            if product.in_stock > 0:
                ProductInBasket.objects.create(product=product, quantity=1)

        return redirect('product-list')


class BasketListView(ListView):
    model = ProductInBasket
    template_name = 'shopapp/basket/basket_list.html'
    context_object_name = 'basket_list'

    def get_context_data(self, **kwargs):
        context = super(BasketListView, self).get_context_data(**kwargs)
        total = 0
        for basket in ProductInBasket.objects.all():
            total += basket.product.price * basket.quantity
        contact_form = ContactForm()
        context['total_price'] = total
        context['form'] = contact_form
        return context


class ProductDeleteFromBasket(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        basket = get_object_or_404(ProductInBasket, pk=pk)
        basket.delete()
        return redirect('basket-list')


class ProductBuyConfirm(View):
    def post(self, request, *args, **kwargs):
        baskets = ProductInBasket.objects.all()
        form = ContactForm(request.POST)
        if form.is_valid():
            cn_data = form.cleaned_data
            name = cn_data['name']
            phone_number = cn_data['phone_number']
            address = cn_data['address']
            products = []
            for basket in baskets:
                products.append(basket.product)
            order = Order.objects.create(
                name=name, phone_number=phone_number, address=address)
            order.products.add(*products)
            order.save()

            for basket in baskets:
                OrderProduct.objects.create(
                    order=order, product=basket.product, quantity=basket.quantity, name=name, phone_number=phone_number, address=address)
                basket.product.in_stock = basket.product.in_stock - basket.quantity
                basket.product.save()
                basket.delete()
        return redirect('product-list')
