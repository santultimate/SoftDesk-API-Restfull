from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

def validate_age(value):
    if value < 15:
        raise ValidationError("L'âge minimum requis est de 15 ans.")

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, validators=[validate_age])
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=True)

    def __str__(self):
        return self.username
