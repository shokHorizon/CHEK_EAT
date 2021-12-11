from django.shortcuts import render

def restaraunts(request):
    context = {}

    if request.user.is_authenticated():
        content

    return render(request, 'restaraunts/restaraunts.html')
