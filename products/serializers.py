# from rest_framework import serializers
# from .models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['date', 'name', 'nutrition_grade', 'url', 'category', 'substitut', 'id', 'favorite'] 
        
from rest_framework import serializers
from .models import Product, MyFavorites

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['date', 'name', 'nutrition_grade', 'url', 'category', 'id', 'favorite'] 
        
class FavoritesSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=255, min_length=3)
    
    class Meta:
        model = MyFavorites
        fields = ['user', 'sub_product', 'old_product'] 
        