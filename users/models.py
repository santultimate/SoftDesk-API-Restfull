from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUser(AbstractUser):

    
    age= models.PositiveIntegerField(null=True, blank=True)
    phone= models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.email
