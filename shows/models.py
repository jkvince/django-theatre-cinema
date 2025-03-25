from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import CustomUser

class Show(models.Model):

    show_id = models.SlugField(
        primary_key=True
    )
    show_name = models.CharField(
        max_length=200
    )
    show_type = models.CharField(
        max_length=30
    )
    show_duration = models.IntegerField()
    show_description = models.TextField()
    show_agerating = models.CharField(
        max_length=20
    )
    show_release_date = models.DateField()
    show_language = models.CharField(
        max_length=20
    )
    show_banner = models.ImageField()
    public = models.BooleanField()

    def __str__(self):
        return self.show_id


class ShowMember(models.Model):
    show_member_id = models.SlugField(
        primary_key=True
    )
    show_member_type = models.CharField(
        max_length=20
    )
    show_member_name = models.CharField(
        max_length=50
    )
    show_member_banner = models.ImageField()
    public = models.BooleanField()

    def __str__(self):
        return self.show_member_id


class MemberJunction(models.Model):
    member_junction_id = models.AutoField(
        primary_key=True
    )
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    show_member = models.ForeignKey(ShowMember, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_junction_id


class Comment(models.Model):
    comment_id = models.UUIDField(
        primary_key=True
    )
    comment_content = models.TextField()
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_id


class Rating(models.Model):
    rating_id = models.IntegerField(
        primary_key=True
    )
    rating_value = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating_id


class Following(models.Model):
    following_id = models.IntegerField(
        primary_key=True
    )
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.following_id


class Tag(models.Model):
    tag_name = models.CharField(
        max_length=30
    )
    show = models.ManyToManyField(Show)

    def __str__(self):
        return self.tag_name