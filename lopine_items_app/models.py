from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20, unique=True, default='DEU')

    def __str__(self):
        return self.name


class Rulesystem(models.Model):
    name = models.CharField(max_length=20, unique=True, default='DSA4.1')

    def __str__(self):
        return self.name


class ItemType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ItemPlace(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ItemRarity(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ItemCondition(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ItemStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    rulesystem = models.ForeignKey(Rulesystem, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    item_type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True)
    item_place = models.ForeignKey(ItemPlace, on_delete=models.SET_NULL, null=True)
    weight_percentage = models.IntegerField(default=500, validators=[MaxValueValidator(950)], help_text='500 = 50%')
    name = models.CharField(max_length=255, unique=True,
                            help_text='Specific Item Name like Rusty Dagger, Sweet Bread or Leather Shirt')
    rarity = models.ForeignKey(ItemRarity, on_delete=models.SET_NULL, null=True)
    max_count = models.IntegerField(validators=[MinValueValidator(1)], default=1,
                                    help_text='How many can be max found while Looting')
    condition = models.ForeignKey(ItemCondition, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(ItemStatus, on_delete=models.SET_NULL, null=True)
    status_note = models.CharField(max_length=255, default='None')
    weight_gram = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    price_gold = models.FloatField(default=1, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Color(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='colors')
    color_name = models.CharField(max_length=255)

    def __str__(self):
        return self.color_name


class Material(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='material')
    material_name = models.CharField(max_length=255)

    def __str__(self):
        return self.material_name
