from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    context = {}
    return render(request, 'user/index.html')

def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except Exception:
            messages.error(request, 'Пользователь не зарегистрирован')
            return redirect('index')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('restaraunts')
        else:
            messages.error(request, 'Ведён неправильный логин и/или пароль')


    context = {}
    return render(request, 'user/index.html')

def registerUser(request):
    context = {}
    return render(request, 'index.html')

def logoutUser(request):
    logout(request)
    context = {}
    return redirect('index')
