from django.shortcuts import render

def restaraunts(request):
    context = {}

    if request.user.is_authenticated:
        pass

    return render(request, 'restaraunts/restaraunts.html')

def create_restaraunt(request):
    context = {}

    if request.method == 'POST':
        test = request.POST.get('place-location')
        print(test)

    return render(request, 'restaraunts/create.html', context)
