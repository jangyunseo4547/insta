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