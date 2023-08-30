from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create(self, phone=None, email=None, password=None, **extra_fields):
        if not (phone or email):
            raise ValueError('Provide at least phone or email')
        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create(phone, email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True)
    fullname=models.CharField(max_length=100,null=True,blank=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['phone']
    objects=UserManager()
    