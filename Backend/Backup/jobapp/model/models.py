from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    table_columns = models.CharField(max_length=200)
    table_data = models.CharField(max_length=400)