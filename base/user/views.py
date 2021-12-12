from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    context = {}
    return render(request, 'user/index.html', context)

def waiter(request):
    context = {}
    return render(request, 'user/waiter.html', context)

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
    return render(request, 'user/index.html', context)

def registerUser(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            redirect('restaraunts')
        else:
            messages.error(request, 'Ошибка при регистрации')

    context = {}
    return redirect('index')

def logoutUser(request):
    logout(request)
    context = {}
    return redirect('index')


def crm(request):
    context = {}
    return render(request, 'user/crm.html', context)

