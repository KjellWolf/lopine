from django.urls import path
from . import views

urlpatterns = [
    path('lootgen', views.show_lootgen, name='lootgen'),
    #path('wetter.html', views.error404, name='wetter.html'),
    # Add other URL patterns as needed
]