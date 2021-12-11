from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    context = {}
    return render(request, 'index.html')

def loginUser(request):
    context = {}
    return render(request, 'index.html')

def registerUser(request):
    context = {}
    return render(request, 'index.html')

def logoutUser(request):
    context = {}
    return render(request, 'index.html')
