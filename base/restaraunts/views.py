from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

def restaraunts(request):
    context = {}

    if request.user.is_authenticated:
        pass

    return render(request, 'restaraunts/restaraunts.html')

@csrf_protect
def create_restaraunt(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('title')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        table_location = request.POST.getlist('place-location')
        table_persons = request.POST.getlist('persons-number')
        table_numbers = request.POST.getlist('tables-number')
        print(name, address, phone, table_location, table_numbers, table_persons)

    return render(request, 'restaraunts/create.html', context)
