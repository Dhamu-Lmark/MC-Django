from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    reset_password_token = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)  # Note: Not recommended for production, use hashing

    def __str__(self):
        return self.username

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'