from django.db import models

class User(models.Model):
    username = models.CharField()
    password = models.CharField(max_length=100)
    table_columns = models.CharField(max_length=200)
    table_data = models.CharField(max_length=400)
    
    def __str__(self) -> str:
        return self.username