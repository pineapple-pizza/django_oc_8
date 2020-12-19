from rest_framework import routers
from .views import RegisterView, VerifyEmail, LoginAPIView
from django.urls import path
# from .api import UserViewset

# router = routers.DefaultRouter()
# router.register('api/auth', UserViewset, 'auth')

# urlpatterns = router.urls


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('login/', LoginAPIView.as_view(), name='login'),
]