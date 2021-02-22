from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def board(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'detail.html', {'post':post})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.content = request.POST['content']
    new_post.save()
    return redirect('detail', new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'edit.html', {'post':edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.pub_date = timezone.now()
    update_post.content = request.POST['content']
    update_post.save()
    return redirect('detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('board')