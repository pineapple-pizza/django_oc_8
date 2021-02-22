# from .test_setup import TestSetUpProducts
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
# from authentication.models import User
from products.models import Product
from rest_framework.authtoken.models import Token
# from products.test.product_factory import ProductFactory

# class TestViewsProducts(APITestCase):
#     def test_create_product(self, client) -> None:
#         assert Product.objects.count() == 0
#         product: Product = ProductFactory()
#         response = client.post(
#             "/products/",
#             product
#         )
#         assert response.status_code == 201, response.data
#         assert Product.objects.count() == 1
        