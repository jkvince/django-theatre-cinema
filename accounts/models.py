from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse

class CustomUser(AbstractUser):
    # username
    # password
    # email
    phone = models.CharField(max_length=15)
    is_premium = models.BooleanField(
        default=False
    )
    profile_pic = models.ImageField(upload_to="media/profile_pic", max_length=200)
