from django.shortcuts import render

def show_main(request):
    context = {
        'app name' : 'Corner Store Inventory',
        'name' : 'Alex Panfilov',
        'class' : 'PBP KI'
    }

    return render(request, "main.html", context)
