from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    city = models.CharField(max_length=100, default="Lagos", blank=True, null=True)
    state = models.CharField(max_length=100, default="Lagos", blank=True, null=True)
    address = models.TextField(blank=True, default="3, Cole Street, Ajah, Lagos", null=True)
    phone = models.CharField(max_length=15, default="012345678", blank=True, null=True)

    def __str__(self):
        return self.username