from .test_setup import TestSetUp
from ..models import User 
# from products.models import Product

class TestViews(TestSetUp):
    def test_user_cannot_register(self):
        """registration with no data """
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)
        
    def test_user_can_register(self):
        """registration with data """
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 201)
        
    def test_user_cannot_login(self):
        """login with an unverified email """
        self.client.post(self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 401)
        
    def test_user_can_login_after_verif(self):
        """login with a verified email """
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)
        