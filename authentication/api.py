from project.models import User 
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

# user viewset
# class UserViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = UserSerializer