from django.db import models

from users.models import UserAccount
from products.models import Category, Products
# Create your models here.

ORDER_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
]

class Order(models.Model):
    customer = models.ForeignKey(UserAccount, on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    order_status = models.CharField(choices = ORDER_STATUS, max_length = 10, default = "Pending")
    cancel = models.BooleanField(default = False)
    
    
    
    
        