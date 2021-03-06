from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer, FavoritesSerializer
from .models import Product, MyFavorites
from rest_framework import permissions
# from .permissions import IsOwner
from rest_framework.filters import SearchFilter, OrderingFilter

class ProductListAPIView(ListCreateAPIView):
    """ products class CRUD methods"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'category')
    
    def perform_create(self, serializer):
        # return serializer.save(owner=self.request.user)
        return serializer.save()
    
    def get_queryset(self):
        # return self.queryset.filter(owner = self.request.user)
        return self.queryset.filter()
    
class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    """ on product by id """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    
    def perform_create(self, serializer):
        # return serializer.save(owner=self.request.user)
        return serializer.save()
    
    def get_queryset(self):
        # return self.queryset.filter(owner = self.request.user)
        return self.queryset.filter()
    
class FavoritesAPIView(ListCreateAPIView):
    serializer_class = FavoritesSerializer
    queryset = MyFavorites.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_queryset(self):
        # products = Product.objects.all()
        return self.queryset.filter(user = self.request.user)
        
        # obj = MyFavorites.objects.get(id=1)
        # # obj.substitut_set.all()
        # obj.substitut_set.all()
        # return obj
        # return self.queryset.filter(user=self.request.user)
        # return self.products.filter(name = sub_product)
        
        # fav_ids = Product.objects.filter(name='Pizza royale')
        # fav = MyFavorites.objects.filter(id__in=fav_ids)
        
        # return fav