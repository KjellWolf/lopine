from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Item, Color, Material, ItemPlace, ItemType, Language, Rulesystem, ItemRarity, ItemCondition, \
    ItemStatus
from django.forms import inlineformset_factory

ColorFormSet = inlineformset_factory(Item, Color, fields=('color_name',))

MaterialFormSet = inlineformset_factory(Item, Material, fields=('material_name',))


@admin.register(ItemPlace)
class ItemPlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Rulesystem)
class RulesystemAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ItemRarity)
class RulesystemAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ItemCondition)
class RulesystemAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ItemStatus)
class RulesystemAdmin(admin.ModelAdmin):
    list_display = ('name',)


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

    search_fields = ('name', 'status_note')

    ordering = ('name',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('rulesystem', 'language', 'weight_percentage', 'item_type')
        }),
        ('Item Main Info', {
            'fields': ('name', 'rarity', 'max_count', 'item_place')
        }),
        ('Item Details', {
            'fields': ('condition', 'status', 'status_note', 'weight_gram', 'price_gold')
        }),
    )


admin.site.register(Item, ItemAdmin)
