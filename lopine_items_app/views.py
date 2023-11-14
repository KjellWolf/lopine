from django.shortcuts import render


# Create your views here.
def show_lootgen(request):
    return render(request, 'lopine_items_app/lootgen.html')
