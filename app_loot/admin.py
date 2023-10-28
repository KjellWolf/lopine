# imports
from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('Name (*)', 'item_typ', 'rarity', 'max_count', 'condition', 'Status (*)')
    list_filter = ('item_typ', 'rarity', 'condition', 'Status (*)')
    search_fields = ('item_name',)
    list_per_page = 20  # Customize the number of items displayed per page


admin.site.register(Item, ItemAdmin)
