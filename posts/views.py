from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    posts = Post.objects.all()
    form = CommentForm()
    context = {
        'posts':posts,
        'form':form,
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)   # 유저 정보가 빠져있음.
            post.user = request.user
            post.save()
            return redirect('posts:index')
    
    else:
        form = PostForm()
    context = {
        'form':form,
    }

    return render(request, 'create.html', context)

@login_required
def comment_create(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id # 댓글 달 게시글 찾기
        comment.save()
        return redirect('posts:index')

@login_required
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)

#1) 유저 관점
    if user in post.like_users.all(): # 좋아요가 눌려 있으면 좋아요 제거
        post.like_users.remove(user)   
    else:
        post.like_users.add(user) # 좋아요 눌리지 않으면 누르기
    
    return redirect('posts:index')

#2) 게시글 관점
    # if post in user.like_posts.all():
    #     user.like_posts.remove(post)
    # else:
    #     user.like_posts.add(post)

def feed(request):
    followings = request.user.followings.all() # 내가 팔로우 하는 사람들 목록
    posts = Post.objects.filter(user__in=followings) # 내가 팔로우 하는 사람들이 작성한 게시글
    
    form = CommentForm()

    context = {
        'posts':posts,
        'form':form,
    }
    return render(request, 'index.html', context)
