from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    is_premium = models.BooleanField(
        default=False
    )
    profile_pic = models.ImageField(upload_to="media/profile_pic", max_length=200)

    class Meta:
        ordering = ('username',)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return str(self.id)