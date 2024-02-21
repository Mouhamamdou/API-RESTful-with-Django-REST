from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):
    age = models.IntegerField(default=18)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    created_time = models.fields.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.age < 15:
            raise ValidationError("moins de 15 ans")
        super().save(*args, **kwargs)

