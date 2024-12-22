from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("posts_list")
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("posts_list")
            else:
                form.add_error("username", "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "user/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")