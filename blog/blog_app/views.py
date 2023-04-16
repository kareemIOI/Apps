from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        user = User.objects.create_user(self, username, email, phone, message)
        user.save()
        print("user is online and user is {user}")
        return redirect("/")
