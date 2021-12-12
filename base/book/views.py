from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from restaraunts.models import Restaraunt

def booking(request):
    context={'restaurants': Restaraunt.objects.all()}

    return render(request, 'book/booking.html', context)


def book(request):
    return render(request, 'book/book.html')

def confirm(request):
    pass

