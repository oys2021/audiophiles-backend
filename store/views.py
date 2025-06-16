from rest_framework import generics
from store.models import Product, Order
from store.serializers import ProductSerializer, OrderSerializer,ProductDetailSerializer
from rest_framework.generics import RetrieveAPIView

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class NewProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_new=True)
    serializer_class = ProductSerializer

class SpeakerListView(generics.ListAPIView):
    queryset = Product.objects.filter(category='Speakers')
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class HeadphoneListView(generics.ListAPIView):
    queryset = Product.objects.filter(category='Headphones')
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EarphoneListView(generics.ListAPIView):
    queryset = Product.objects.filter(category='Earphones')
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}



class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

