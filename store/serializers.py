import os
from rest_framework import serializers
from .models import Product, Category, Order, OrderItem,ProductGallery

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    image_absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 'is_new', 'category', 'image', 'image_absolute_url'
        ]

    def get_image_absolute_url(self, obj):
        request = self.context.get('request')
        filename = os.path.basename(obj.image.name)
        return request.build_absolute_uri(f'/static/media/products/{filename}')

class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ['id', 'image']

        

class ProductDetailSerializer(serializers.ModelSerializer):
    gallery = ProductGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price','description','image', 'gallery']



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'full_name', 'email', 'address', 'city', 'country', 'zip_code', 'total', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        return order
