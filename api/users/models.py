from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from common.models import BaseModel

# Create your models here.
class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_superuser
    @is_staff.setter
    def is_staff(self, value):
        self.is_superuser = value
