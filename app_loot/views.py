from django.shortcuts import render
from .models import Item


def item_list(request):
    items = Item.objects.all()  # Query all Item objects
    context = {'items': items}  # Create a context dictionary with the data
    return render(request, 'view_app_loot_data.html', context)
