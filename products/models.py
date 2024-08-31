from django.db import models
from users.models import UserAccount

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_slug = models.SlugField(max_length = 50)
    def __str__(self):
        return self.category_name
    
class Products(models.Model):
    category = models.ManyToManyField(Category)
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(max_length = 100)
    product_image = models.ImageField(upload_to="products/images/")
    product_description = models.TextField()
    product_price = models.FloatField()
    product_quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.product_name

    
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(UserAccount, on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"Reviewer : {self.reviewer.user.first_name} | Product Name : {self.product.product_name}"
    