from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('member', 'Member'),
        ('trainer', 'Trainer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    phone = models.CharField(max_length=20, blank=True)