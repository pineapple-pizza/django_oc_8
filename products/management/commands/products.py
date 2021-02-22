from django.core.management.base import BaseCommand, CommandError
import requests, json
from products.models import Product
from django.utils import timezone

class Command(BaseCommand):
    help = 'display all products'

    def add_products(self):
        
        url = 'https://fr-en.openfoodfacts.org/category/pizza.json'
        response = requests.get(url)
        products_data = response.json()
        products = products_data['products']
        
        nutriscore = ''
        prod_name = ''
        prod_url = ''
        
        for i in range(len(products)):
            if not products[i]['nutriscore_grade']:
                print('error')
            if products[i]['nutriscore_grade']:
                nutriscore = products[i]['nutriscore_grade']
                print('nutriscore: ', nutriscore)
            
            if not products[i]['url']:
                print('error')
            if products[i]['url']:
                prod_url = products[i]['url']
                print('url: ', prod_url)
            
            prod_name = products[i]['product_name']
            print('prod name: ', prod_name)
            
            data = Product(name=prod_name, url=prod_url, nutrition_grade=nutriscore, category="pizza", date=timezone.now())
            data.save()
        return products
        
        
    def handle(self, *args, **kwargs):
        
        self.add_products()