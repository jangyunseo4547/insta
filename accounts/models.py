from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.

# 유저
class User(AbstractUser):
    # username
    # passward
    profile_image = ResizedImageField(
        size = [500,500],
        crop = ['middle', 'center'],
        upload_to = 'profile',
    )
    # post_set
    # comment_set