from django.shortcuts import render,redirect
from .models import Post,Cast
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_lists(request):
    posts=Post.objects.all()
    return render(request,'posts/posts_list.html',{'posts':posts})

def post_page(request,slug):
    post=Post.objects.get(slug=slug)
    casts=Cast.objects.filter(post=post)
    return render(request,'posts/posts_page.html',{'post':post,'casts':casts})

@login_required(login_url="/users/login/")
def like_page(request,slug):
    post=Post.objects.get(slug=slug)
    post.likes+=1
    post.save()
    return redirect('posts:page',slug=slug)
