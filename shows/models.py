from django.db import models
import uuid

class Show(models.Model):
    
    show_id = models.SlugField(
        primary_key=True
    )
    show_name = models.CharField()
    show_type = models.CharField()
    show_duration = models.IntegerField()
    show_description = models.TextField()
    show_agerating = models.CharField()
    show_release_date = models.DateField()
    show_language = models.CharField()
    show_barrier = models.ImageField()


class ShowMember(models.Model):
    show_member_id = models.SlugField(
        primary_key=True
    )
    show_member_type = models.CharField()
    show_member_name = models.CharField()
    show_member_banner = models.ImageField()


class MemberJunction(models.Model):
    member_junction_id = models.AutoField(
        primary_key=True
    )
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    show_member = models.ForeignKey(ShowMember, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_id = models.UUIDField(
        primary_key=True
    )
    comment_content = models.TextField()
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    user_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Rating(models.Model):
    rating_id = models.UUIDField(
        primary_key=True
    )
    rating_value = models.IntegerField()
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    user_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Following(models.Model):
    following_id = models.IntegerField(
        primary_key=True
    )
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    user_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    