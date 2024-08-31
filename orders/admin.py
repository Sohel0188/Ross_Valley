from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from .import models

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'customer', 'order_status', 'cancel']
    def product_name(self,obj):
        return obj.product.product_name
    
    def product_price(self,obj):
        return obj.product.product_price
    
    def customer(self,obj):
        return obj.customer.users.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.order_status == "Processing" or "Completed":
            email_subject = "Order Status"
            email_body = render_to_string('orderEmail.html', {'user' : obj.customer.user})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.customer.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
    
admin.site.register(models.Order, OrderAdmin)