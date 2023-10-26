from django.contrib import admin
from .models import Item, ItemDetails

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_typ', 'rarity', 'max_count', 'condition', 'status')
    list_filter = ('item_typ', 'rarity', 'condition', 'status')
    search_fields = ('name',)
    list_per_page = 20  # Customize the number of items displayed per page

class ItemDetailsAdmin(admin.ModelAdmin):
    list_display = ('item',)
    search_fields = ('item__name',)  # Search based on the related Item's name

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemDetails, ItemDetailsAdmin)