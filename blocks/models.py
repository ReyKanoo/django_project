from django.db import models
from django.contrib.auth.models import User

class block(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    ROLE_CHOICES = [
        ('reader', 'Посетитель'),
        ('editor', 'Редактор'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='reader')

    def __str__(self):
        return f"{self.user.username} — {self.role}"