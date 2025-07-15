from django.shortcuts import render
from posts.models import Post

def homepage(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def search(request):
    query=request.GET.get('search','')
    posts=Post.objects.filter(title__icontains=query)
    return render(request, 'search.html', {
        'allmovies': posts,
        'query': query
    })