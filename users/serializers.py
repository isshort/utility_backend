from rest_framework import serializers as srz
from users.models import User

class UserListSerializer(srz.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
