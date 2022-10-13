from django.urls import path
from shopapp.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView
    )

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('create/', ProductCreateView.as_view(), name="product-create"),
]