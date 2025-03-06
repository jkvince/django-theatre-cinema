from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse

class CustomUser(AbstractUser):
    # username
    # password
    # email
    # is_staff
    phone = models.IntegerField()
    premium = models.BooleanField(
        default=False
    )
    profile_pic = models.ImageField(upload_to="media/profile_pic", max_length=200)
