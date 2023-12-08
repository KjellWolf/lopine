from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Language(models.Model):
    """

    This class represents a language in the application.

    Attributes:
        name (str): The name of the language. It has a maximum length of 20 characters and must be unique. The default value is 'DEU'.

    Methods:
        __str__(): Returns a string representation of the language.

    """
    name = models.CharField(max_length=20, unique=True, default='DEU')

    def __str__(self):
        return self.name


class Rulesystem(models.Model):
    """
    This class represents a rules system.

    Attributes:
        name (str): The name of the rules system.

    Methods:
        __str__(): Returns a string representation of the rules system.

    """
    name = models.CharField(max_length=20, unique=True, default='DSA4.1')

    def __str__(self):
        return self.name


class ItemType(models.Model):
    """
    Represents an item type.

    Attributes:
        name (str): The name of the item type.
    """
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ItemPlace(models.Model):
    """
    Class representing a place for storing items.

    Attributes:
        name (str): The name of the item place.

    Methods:
        __str__(): Returns a string representation of the item place.

    """
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ItemRarity(models.Model):
    """

    class ItemRarity(models.Model):
        name = models.CharField(max_length=20, unique=True)

        def __str__(self):
            return self.name

    """
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ItemCondition(models.Model):
    """
    Class representing the condition of an item.

    Attributes:
        name (str): The name of the item condition.

    Methods:
        __str__(): Returns the name of the item condition.

    """
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ItemStatus(models.Model):
    """
    The ItemStatus class represents the status of an item.

    Attributes:
        name (str): The name of the item status.

    Methods:
        __str__(): Returns the name of the item status.
    """
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    """

    The Item class represents a specific item in the system.

    Attributes:
    - item_id (AutoField): The unique identifier for the item.
    - rulesystem (ForeignKey): The rulesystem associated with the item.
    - language (ForeignKey): The language associated with the item.
    - item_type (ForeignKey): The type of the item.
    - item_place (ForeignKey): The place of the item.
    - weight_percentage (IntegerField): The weight percentage of the item. Default value is 500.
    - name (CharField): The name of the item. Max length is 255 characters. Unique.
    - rarity (ForeignKey): The rarity of the item.
    - max_count (IntegerField): The maximum count of the item. Default value is 1.
    - condition (ForeignKey): The condition of the item.
    - status (ForeignKey): The status of the item.
    - status_note (CharField): The note for the status of the item. Max length is 255 characters. Default value is 'None'.
    - weight_gram (IntegerField): The weight in grams of the item. Default value is 1.
    - price_gold (FloatField): The price in gold of the item. Default value is 1.

    Methods:
    - __str__: Returns the name of the item.

    """
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
    """
    A class to represent a color.

    Attributes:
        item (ForeignKey): The foreign key to the related Item.
        color_name (CharField): The name of the color.

    Methods:
        __str__(): Returns the name of the color.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='colors')
    color_name = models.CharField(max_length=255)

    def __str__(self):
        return self.color_name


class Material(models.Model):
    """
    Returns the material name.

    :return: A string representing the material name.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='material')
    material_name = models.CharField(max_length=255)

    def __str__(self):
        return self.material_name
