from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=12, unique=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True) #
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username