from itertools import product
from django.urls import path

from shopapp.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
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
         ProductDeleteView.as_view(), name='product-delete')
]
