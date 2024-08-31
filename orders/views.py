from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from . import serializer
from rest_framework import viewsets
from . import models
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

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
        email = serializer.validated_data['email']
        phone = serializer.validated_data['phone']
        print(email);
        if product.product_quantity > 0:
            product.product_quantity -= 1
            product.save()
            email_subject = "Thank You Creating An Order"
            email_body = render_to_string('orderemail.html',{'product' : product.product_name, 'amount' : product.product_price, 'email' : email,'phone':phone})
            email = EmailMultiAlternatives(email_subject , '', to=[email]) 
            email.attach_alternative(email_body, "text/html")
            email.send()
            serializer.save()
            
        else:
            return Response({'error': 'Product out of stock'}, status=status.HTTP_400_BAD_REQUEST)
    
