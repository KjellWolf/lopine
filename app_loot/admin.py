from django.contrib import admin
from .models import Item, Color, Material
from django.forms import inlineformset_factory

ColorFormSet = inlineformset_factory(Item, Color, fields=('color_name',))

MaterialFormSet = inlineformset_factory(Item, Material, fields=('material_name', ))


class ColorInline(admin.StackedInline):
    model = Color
    extra = 1


class MaterialInLine(admin.StackedInline):
    model = Material
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    inlines = [ColorInline, MaterialInLine]

    list_display = (
        'name',
        'item_type',
        'weight_percentage',
        'rarity',
        'max_count',
        'condition',
        'status',
    )

    list_filter = ('item_type', 'rarity', 'condition', 'status')

    search_fields = ('name', 'common_name', 'status_note')

    ordering = ('name',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('rulesystem', 'language', 'item_type', 'name', 'common_name', 'rarity', 'max_count')
        }),
        ('Item Details', {
            'fields': ('condition', 'status', 'status_note', 'weight_gram', 'price_gold')
        }),
    )


admin.site.register(Item, ItemAdmin)
