"""
URL configuration for Lopine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from Lopine.views import user_profile, delete_account_view
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index, name='show_index'),
    path('wetter.html', views.show_maintain, name='maintain'),
    path('404.html', views.show_error404, name='wetter.html'),
    path('', include('lopine_items_app.urls')),
    path('', include('polls.urls')),
    path('', LoginView.as_view(template_name='index.html'), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/profile/', user_profile, name='user_profile'),
    path('delete_account/', delete_account_view, name='delete_account'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

