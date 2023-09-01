from rest_framework import serializers as srz
from rest_framework_simplejwt.serializers import PasswordField
from rest_framework_simplejwt.serializers import \
    TokenRefreshSerializer as BaseRefreshSerializer

from users.models import User


class UserListSerializer(srz.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
class TokenSerializer(BaseRefreshSerializer):
    default_error_messages = {
            'no_active_account': 'No active account found with the given credentials'
    }

    username=srz.CharField(max_length=255)
    password=PasswordField(write_only=True)

