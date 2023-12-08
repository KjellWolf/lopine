from django.shortcuts import render
from .models import Item

# Create your views here.
def show_lootgen(request):

    return render(request, 'lopine_items_app/lootgen.html')
