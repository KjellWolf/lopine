from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.http import Http404
from lopine_items_app.models import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def show_index(request):
    items = Item.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile')  # Redirect to the user profile page after successful login
        else:
            messages.error(request, 'Invalid username or password.')  # Display error message
            return redirect('')  # Redirect back to the login page with error message
    return render(request, 'index.html', {'items': items})


@login_required
def user_profile(request):
    user = request.user  # Get the current logged-in user

    context = {
        'user': user,
    }

    return render(request, 'user_profile.html', context)

@login_required
def delete_account_view(request):
    if request.method == 'POST':

        user = request.user
        user.delete()
        logout(request)  # Logout the user
        return redirect('/')  # Replace 'home' with the URL name for your home page or any other appropriate URL

    return render(request, 'delete_account.html')

def show_maintain(request):
    return render(request, 'maintain.html')


def show_error404(request):
    return render(request, '404.html')
