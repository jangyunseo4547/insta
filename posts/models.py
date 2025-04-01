from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

# 게시글
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    # image = models.ImageField(upload_to = 'image') # image 폴더 생성 후 그 안에 이미지 저장됨 / pillow 설치 !
    image = ResizedImageField(
        size = [500,500], 
        crop = ['middle', 'center'], # 가운데 기준 크롭
        upload_to = 'image/%Y/%m', # 연도와 월을 기준으로 폴더를 만듦.
    )
    # 작성자 연결
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    
    # 좋아요를 누른 사람 연결
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='like_posts',
        ) # User와 Post를 M:N으로 연결

# 댓글
class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)