from django.db import models
from authentication.models import User

# Create your models here.

class Product(models.Model):
    
    CATEGORY_OPTIONS = [
        ('sauces', 'sauces'),
        ('desserts', 'desserts'),
        ('seafood', 'seafood'),
        ('biscuits', 'biscuits'),
        ('french_cheese', 'french_cheese'),
        ('pizza', 'pizza'),
    ]
    
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    # name = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    name = models.CharField(max_length=255)
    url = models.TextField()
    nutrition_grade = models.CharField(max_length=255)
    substitut = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_created=True)
    favorite = models.BooleanField(default=False)