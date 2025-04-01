## insta
project : insta
app : posts

## 게시글 생성
`python manage.py createsuperuser`

## image 폴더를 .gitignore로 관리하지 않음.
- image/ 

## 새로운 라이브러리 추가 시  
`pip freeze >> requirements.txt` : 추가 
`pip freeze > requirements.txt` : 꺽쇠를 한번만 하면 이전거에 덮어쓰여짐.

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
<form action="" method="POST" enctype="multipart/form-data"> 
#enctype 설정해줘야 함.

# -> FILES에 저장됨.
```

## db 지우고 모델 -> 마이그레션하기


## django_session : 사용자 정보가 담김.

## timesince : 몇초 전 
`_card.html` : |timesince

## div.row
- col-12 : 12개의 칸으로 나눠짐.
- xs, sm, md, lg, xl : 크기 설정
- <div class="row"> : 가로로 길게 해줌.
- wrapper_class='' : 위아래 간격 맞추기


