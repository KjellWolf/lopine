from django.shortcuts import render
from django.http import Http404


def show_index(request):
    return render(request, 'index.html')


