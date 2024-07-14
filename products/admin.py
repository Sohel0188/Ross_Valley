from django.contrib import admin
from . import models 
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug': ('product_name',), }
    
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('category_name',), }
    
admin.site.register(models.Products,ProductsAdmin)
admin.site.register(models.Category,CategoriesAdmin)
admin.site.register(models.Review)