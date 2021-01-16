from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['date', 'name', 'nutrition_grade', 'url', 'category', 'substitut', 'id', 'favorite'] 
        