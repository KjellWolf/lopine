from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'item_id',
        'name',
        'item_type',
        'weight_percentage',
        'rarity',
        'max_count',
        'material',
        'color',
        'condition',
        'status',
    )

    list_filter = ('item_type', 'rarity', 'condition', 'status')

    search_fields = ('name', 'common_name', 'material', 'color', 'status_note')

    list_editable = (
        'name', 'item_type', 'weight_percentage', 'rarity', 'max_count', 'material', 'color', 'condition', 'status')

    ordering = ('name',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('rulesystem', 'item_type', 'name', 'common_name', 'rarity', 'max_count')
        }),
        ('Item Details', {
            'fields': ('material', 'color', 'condition', 'status', 'status_note', 'weight_gram')
        }),
    )


admin.site.register(Item, ItemAdmin)
