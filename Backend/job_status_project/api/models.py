from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    table_columns = models.JSONField()
    table_data = models.JSONField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.username