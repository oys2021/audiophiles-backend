from django.urls import path
from .views import ProductListView, ProductDetailView, OrderCreateView,SpeakerListView,EarphoneListView,HeadphoneListView,NewProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('newproducts/', NewProductListView.as_view(), name='newproduct-list'),
    path('speakers/', SpeakerListView.as_view(), name='speaker-list'),
    path('headphones/', HeadphoneListView.as_view(), name='headphone-list'),
    path('earphones/', EarphoneListView.as_view(), name='earphone-list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
]
