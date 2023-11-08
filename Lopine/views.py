from django.shortcuts import render
from django.http import Http404


def show_index(request):
    return render(request, 'index.html')


def show_maintain(request):
    return render(request, 'maintain.html')


def show_error404(request):
    return render(request, '404.html')
