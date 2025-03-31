from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    # image = models.ImageField(upload_to = 'image') # image 폴더 생성 후 그 안에 이미지 저장됨 / pillow 설치 !
    image = ResizedImageField(
        size = [500,500], 
        crop = ['middle', 'center'], # 가운데 기준 크롭
        upload_to = 'image/%Y/%m', # 연도와 월을 기준으로 폴더를 만듦.
    )