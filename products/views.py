from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer
from rest_framework import filters

# Create your views here.
class ProcuctsViewset(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializer.ProductsSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        cat_id = self.request.query_params.get('category_id')
        if cat_id :
            queryset = queryset.filter(cat_id=cat_id)
        return queryset
    
class CategoriesViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializer.ReviewSerializer