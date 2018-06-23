from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'members/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        return redirect('signup-result')
    return render(request, 'members/signup.html')

def signup_result(request):
    return render(request, 'members/signup_result.html')