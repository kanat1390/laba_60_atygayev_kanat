from itertools import product
from django.urls import path

from shopapp.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductAddToBasket,
    BasketListView,
    ProductDeleteFromBasket,
    ProductBuyConfirm
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/',
         ProductDetailView.as_view(), name='product-detail'),
    path('products/create/',
         ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/',
         ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/',
         ProductDeleteView.as_view(), name='product-delete'),
    path('products/<int:pk>/to-basket/',
         ProductAddToBasket.as_view(), name='add-product-to-basket'),
    path('baskets/', BasketListView.as_view(), name='basket-list'),
    path('baskets/<int:pk>/delete/',
         ProductDeleteFromBasket.as_view(), name='basket-delete'),
    path('baskets/confirm/',
         ProductBuyConfirm.as_view(), name='basket-confirm')
]
