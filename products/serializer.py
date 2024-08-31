from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Category
        fields = '__all__'
        
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        # fields = ['product_name', 'product_slug', 'product_image','product_description','product_price','product_quantity']
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'