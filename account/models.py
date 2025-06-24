from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=300, unique=True)
    is_active = models.BooleanField(default=True)
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()


    def __str__(self):

        return self.full_name