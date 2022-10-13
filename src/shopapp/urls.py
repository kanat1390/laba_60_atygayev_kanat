from django.urls import path
from shopapp.views import (
    ProductListView,
    ProductDetailView
    )

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]