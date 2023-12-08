from django.shortcuts import render
from django.http import Http404
from lopine_items_app.models import Item

def show_index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def show_maintain(request):
    return render(request, 'maintain.html')


def show_error404(request):
    return render(request, '404.html')
