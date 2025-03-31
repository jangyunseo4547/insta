## insta
project : insta
app : posts

## 게시글 생성
`python manage.py createsuperuser`

## image 폴더를 .gitignore로 관리하지 않음.
- image/ 

## 새로운 라이브러리 추가 시  
`pip freeze >> requirements.txt`

## MEDIA 경로 설정
`settings.py`
```python
# 업로드한 사진을 저장한 위치(실제 폴더 경로)
MEDIA_ROOT = BASE_DIR / 'media'

# image 폴더로 들어오기까지의 (경로)
MEDIA_URL = '/media/'
```

`프로젝트 내 urls.py`
```python
from django.conf.urls.static import static # url이 들어올때의 경로 설정
from django.conf import settings # settings에 작성된 MEDIA_URL 활용

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #concat / 경로 - 저장한 실제 위치
```

## 모듈화 
`_card.html`
`_nav.html`

## 파일 설정 시 
```python 
<form action="" method="POST" enctype="multipart/form-data"> #enctype 설정해줘야 함.

# -> FILES에 저장됨.
```