from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Note: Not recommended for production, use hashing

    def __str__(self):
        return self.username