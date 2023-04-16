from django.shortcuts import render, redirect

from .models import Post

from django.contrib import messages

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        details = request.POST["details"]
        Post.objects.create(title=title, details=details)
        messages.success(request, "data has been added successfully")

    return render(request, "add.html")


def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        details = request.POST["details"]
        Post.objects.filter(id=id).update(title=title, details=details)
        messages.success(request, "data has been updated successfully")

    post = Post.objects.get(id=id)
    return render(request, "update.html", {"post": post})


def delete(request, id):

    Post.objects.filter(id=id).delete()
    return redirect("/")
