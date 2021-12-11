from django.shortcuts import render

def restaraunts(request):
    return render(request, 'restaraunts/restaraunts.html')
