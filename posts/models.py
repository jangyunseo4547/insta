from django.db import models


# Create your models here.
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'image') # image 폴더 생성 후 그 안에 이미지 저장됨 / pillow 설치 ! 