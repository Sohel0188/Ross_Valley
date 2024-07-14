from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from . import serializer
from rest_framework import viewsets
from . import models
class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializer.OrderSerializers
    
    def get_queryset(self):
        queryset = super().get_queryset() 
        customer_id = self.request.query_params.get('customer_id')
        if customer_id:
            queryset = queryset.filter(customer_id=customer_id)
        return queryset
    
    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        if product.product_quantity > 0:
            product.product_quantity -= 1
            product.save()
            serializer.save()
        else:
            return Response({'error': 'Product out of stock'}, status=status.HTTP_400_BAD_REQUEST)
    
