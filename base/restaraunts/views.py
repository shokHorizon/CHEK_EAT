from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Restaraunt, TableType, Table
from django.http import JsonResponse


def restaraunts(request):
    context = {}

    if request.user.is_authenticated:
        context={'restaurants': Restaraunt.objects.filter(owner=request.user)}

    return render(request, 'restaraunts/restaraunts.html', context)


@csrf_protect
def create_restaraunt(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('title')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        start = request.POST.get('start')
        end = request.POST.get('end')

        table_location = request.POST.getlist('place-location')
        table_persons = request.POST.getlist('persons-number')
        table_numbers = request.POST.getlist('tables-number')

        if all((name, address, phone, start, end)):
            restaurant = Restaraunt(
                name=name,
                address=address,
                phone=phone,
                open_time=start,
                close_time=end,
                owner=request.user,
            )

            if restaurant:
                restaurant.save()


                if (len(table_location) ==
                    len(table_numbers) ==
                    len(table_persons) != 0 and
                    all(table_location) and
                    all(table_numbers) and
                    all(table_persons)):

                    for i in range(len(table_location)):
                        tableType = TableType(
                            name=table_location[i],
                            restaurant=restaurant,
                            persons=table_persons[i]
                        )

                        if tableType:
                            tableType.save()

                            for j in range(int(table_numbers[i])):
                                table = Table(
                                    bookedTime=0,
                                    tableType=tableType
                                )

                                if table:
                                    table.save()

            return redirect('restaraunts')


    return render(request, 'restaraunts/create.html', context)


def delete_restaraunt(request, pk):
    context = {}

    if request.user.is_authenticated:
        restaraunt = Restaraunt.objects.filter(owner=request.user, id=pk)
        if restaraunt:
            restaraunt.delete()

    context = {'restaurants': Restaraunt.objects.filter(owner=request.user)}

    return redirect('restaraunts')


def update_restaraunt(request, pk):
    restaraunt = Restaraunt.objects.filter(owner=request.user, id=pk)
    if restaraunt:

        if request.method == 'POST':
            name = request.POST.get('title')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            start = request.POST.get('start')
            end = request.POST.get('end')

            table_location = request.POST.getlist('place-location')
            table_persons = request.POST.getlist('persons-number')
            table_numbers = request.POST.getlist('tables-number')

            if all((name, address, phone, start, end)):
                restaraunt.update(
                    name=name,
                    address=address,
                    phone=phone,
                    open_time=start,
                    close_time=end,
                    owner=request.user,
                )

                if (len(table_location) ==
                        len(table_numbers) ==
                        len(table_persons) != 0 and
                        all(table_location) and
                        all(table_numbers) and
                        all(table_persons)):

                    restaraunt.get().tabletype_set.all().delete()

                    for i in range(len(table_location)):
                        tableType = TableType(
                            name=table_location[i],
                            restaurant=restaraunt.get(),
                            persons=table_persons[i]
                        )

                        if tableType:
                            tableType.save()

                            for j in range(int(table_numbers[i])):
                                table = Table(
                                    bookedTime=0,
                                    tableType=tableType
                                )

                                if table:
                                    table.save()

                return redirect('restaraunts')

        context = {'restaraunt': restaraunt.get()}
    else:
        return redirect('restaraunts')


    return render(request, 'restaraunts/create.html', context)


def get_tables(request, pk):
    context = {}

    if request.method=="GET":
        rest = Restaraunt.objects.filter(id=pk)
        if any(rest):
            rest = rest.get()
            tabletypes = rest.tabletype_set.all()
            for tabletype in tabletypes:
                tables = tabletype.table_set.all()
                tabletimes = [(table.id, table.bookedTime) for table in tables]

                context[tabletype.id] = {
                    'start': rest.open_time,
                    'end': rest.close_time,
                    'book_every': rest.book_every,
                    'name': tabletype.name,
                    'persons': tabletype.persons,
                    'tables': tabletimes,
                }
        else:
            context={'error': 'Restaurant does not exist'}
            return JsonResponse(context)

    return JsonResponse(context)
