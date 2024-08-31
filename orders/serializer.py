from rest_framework import serializers
from .models import Order
# from products.serializer import ProductsSerializer

class OrderSerializers(serializers.ModelSerializer):
    # product = ProductsSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['product', 'name', 'email', 'phone','address','order_status']