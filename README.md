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

## 관계설정 다대다 (M:N)
- User - Like (user_id, post_id) - Post 
- error 
```python
Reverse accessor 'User.post_set' 
#post_set(FK)와 post_set(MMF)가 충돌(중복)
# -> post_set => like_posts(MMF)로 post_set 이름을 바꿔줌.

'posts.Post.like_users'이라는 또 다른 게 만들어지려고 함.
```

## 좋아요 기능 구현
`_card.html`
- <span>{{post.like_users.all|length}}명이 좋아합니다.</span> : span 태그
- class="text-reset text-decoration-none" : 링크 색을 기본적으로 검정색으로 바꿈. / 링크 언더바를 취소함.

## Responsive image 
- class="img-fluid"> : 사용자가 줄이면 이미지가 줄어듦. 
- class='rounded-circle' : 둥글게

## 팔로우 기능 구현
- User --- User 연결
    - 일방적인 팔로우 가능 (단방향)

## 프론트 엔드 
- data-*속성 : html에서 data-로 시작하는 사용자 정의 데이터 속성을 만들 수 있음. (javaScript에서 데이터를 저장, 활용하는데 사용)
- `_card.html`
```python
<i class="bi like bi-heart-fill" style="color: red;" data-post-id="{{post.id}}"> # data-post-id : 어느 게시글의 좋아요 버튼인지 구별하기 위해 만든 속성
```

- `index.html`
```shell
<script>
        # 1. html의 좋아요 버튼(i태그)를 모두 가져옴.
        let likeBtns = document.querySelectorAll('i.like') 
        
        # 2. 좋아요 요청 보내는 함수 만들기
        let likeRequest = async (btn, postId) => {    # 버튼, 게시글
            let likeURL = `/posts/${postId}/like-async` 
            # /posts/1/like-async
            
            # 3. 서버에 요청 보내기 & 결과 받기
            let res = await fetch(likeURL) # 서버에 요청 (좋아요 누름)
            let result = await res.json() # 서버가 응답을 보내주면, json 데이터로 바꿈.

            # 4. 좋아요 상태에 따라 버튼 스타일 변경 
            if (result.status) {   # 좋아요가 눌러졌을 경우
                btn.style.color = 'red'
                btn.classList.remove('bi-heart')
                btn.classList.add('bi-heart-fill')
                
            } else {               # 좋아요가 취소된 경우
                btn.style.color = 'black'
                btn.classList.remove('bi-heart-fill')
                btn.classList.add('bi-heart')
            } 
            # 5. 좋아요 개수 자동 업데이트 
            btn.querySelector('span').innerHTML = result.count # i태그 안에 있는 span을 찾아 좋아요 숫자 업데이트
        }    

        # 6. 클릭 이벤트 추가
        likeBtns.forEach(function(likeBtn){ # 모든 좋아요 버튼에 대해 클릭 이벤트 추가
            likeBtn.addEventListener('click', function(e){
                const postId = e.target.dataset.postId   # 눌린 버튼의 data-post-id 값을 가져옴.

                likeRequest(likeBtn, postId) # 가져온 id를 이용해 좋아요 요청 함수 실행
            })
        })


    </script>
```

