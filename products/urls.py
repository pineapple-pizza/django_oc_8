# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.ProductListAPIView.as_view(), name='products'),
#     path('<int:id>', views.ProductDetailAPIView.as_view(), name='product'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='products'),
    path('<int:id>', views.ProductDetailAPIView.as_view(), name='product'),
    path('favorites/', views.FavoritesAPIView.as_view(), name='products'),
]