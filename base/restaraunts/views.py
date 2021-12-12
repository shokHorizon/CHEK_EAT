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
                #tabletimes = [(table.id, table.bookedTime) for table in tables]

                context[tabletype.id] = {
                    'start': rest.open_time,
                    'end': rest.close_time,
                    'book_every': rest.book_every,
                    'name': tabletype.name,
                    'persons': tabletype.persons,
                }
        else:
            context={'error': 'Restaurant does not exist'}
            return JsonResponse(context)

    return JsonResponse(context)


def get_free_time(request, pk):
    context = {}

    if request.method=="GET":
        tabletype = TableType.objects.filter(id=pk)
        if any(tabletype):
            tabletype = tabletype.get()
            rest = tabletype.restaurant
            opened_time = rest.close_time - rest.open_time
            if opened_time != 0:
                times_available = (opened_time * 60) // rest.book_every
                tables = tabletype.table_set.all()

                free_time = tables[0].bookedTime
                for i in tables:
                    free_time = free_time & i.bookedTime

                res = []
                for i in range(rest.open_time*60, rest.close_time*60, rest.book_every):
                    res.append(f'{i//60}:{i%60}')

                for i in range(times_available):
                    if 2**i & free_time:
                        res[i] = True


                context = {'time': res}

            else:
                context = {'error': "Restaurant working 0 HOURS!"}
        else:
            print(TableType.objects.first().id)
            context={'error': 'Table does not exist'}

    return JsonResponse(context)


def get_end_time(request, pk, chosen_time):
    context = {}

    if request.method=="GET":
        tabletype = TableType.objects.filter(id=pk)
        if any(tabletype):
            tabletype = tabletype.get()
            rest = tabletype.restaurant
            opened_time = rest.close_time - rest.open_time
            if opened_time != 0:
                times_available = opened_time * (60 // rest.book_every)
                tables = tabletype.table_set.all()
                max_queue = 0
                max_id = 0

                for table in tables:
                    for i in range(chosen_time,-1,-1):
                        if 2 ** i & table.bookedTime:
                            break
                        if max_queue < chosen_time - i:
                            max_queue = chosen_time - i
                            max_id = table.id

                context = {'time': chosen_time, 'sequence': max_queue, 'id': max_id}

            else:
                context = {'error': "Restaurant working 0 HOURS!"}
        else:
            print(TableType.objects.first().id)
            context={'error': 'Table does not exist'}

    return JsonResponse(context)


def show_menu(request):
    context = {}

    return render(request, 'restaraunts/menu.html', context)
