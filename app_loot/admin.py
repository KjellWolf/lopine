from django.contrib import admin

from .models import Item


class ChoiceInline(admin.TabularInline):
    model = Item
    extra = 3


admin.site.register(Item)