from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class CustomUser(AbstractBaseUser):
    """
    
    Это кастомный класс пользователей, который можно расширять.

    Args:
        AbstractBaseUser (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return self.email