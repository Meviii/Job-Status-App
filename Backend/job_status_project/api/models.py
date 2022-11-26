from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    table_columns = models.CharField(max_length=200)
    table_data = models.CharField(max_length=400)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.username