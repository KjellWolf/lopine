from django.shortcuts import render
from .models import Item





def show_lootgen(request):
    return render(request, 'lootgen.html')
