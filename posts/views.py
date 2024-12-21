from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import random
from posts.models import Post
from posts.forms import PostForm


def hello_view(request):
    return HttpResponse(f"Hello World {random.randint(1, 100)}")


def html_view(request):
    return render(request, "base.html")


def main_view(request):
    return render(request, "base.html")


def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/post_detail.html", context={"post": post})


def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "posts/post_create.html", context={"form": form})
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/posts/")
        else:
            return render(request, "posts/post_create.html", context={"form": form})