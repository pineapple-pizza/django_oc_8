import datetime

from authentication.models import User
from django.urls import reverse
# from faker import Faker
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        # self.fake = Faker()
    
        self.user_data = { 
            'email': "usertest@test.com",
            'username': "usertest",
            'password': "usertest",
            }
        return super().setUp()

    def tearDown(self): 
        return super().tearDown()