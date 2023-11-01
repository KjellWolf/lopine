from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Item(models.Model):
    LANG_CHOICES = (
        ('DEU', 'DEU'),
        ('ENG', 'ENG'),
    )

    SYSTEM_CHOICES = (
        ('DSA4.1', 'DSA4.1'),
        ('DSA5', 'DSA5'),
        ('SR4', 'SR4'),
        ('SR5', 'SR5'),
    )

    ITEM_TYP_CHOICES = (
        ('Household', 'Household'),
        ('Nature_Material', 'Nature_Material'),
        ('Food', 'Food'),
        ('Lighting', 'Lighting'),
        ('Books', 'Books'),
        ('Eating Utensils', 'Eating Utensils'),
        ('Vehicles', 'Vehicles'),
        ('Vehicle Accessories', 'Vehicle Accessories'),
        ('Precision Mechanics', 'Precision Mechanics'),
        ('Long-range Weapons', 'Long-range Weapons'),
        ('Leisure Needs', 'Leisure Needs'),
        ('Spices', 'Spices'),
        ('Poisons', 'Poisons'),
        ('Medicinal Herbs', 'Medicinal Herbs'),
        ('Chains', 'Chains'),
        ('Clothing', 'Clothing'),
        ('Personal Care', 'Personal Care'),
        ('Ammunition', 'Ammunition'),
        ('Musical Instruments', 'Musical Instruments'),
        ('Melee Weapons', 'Melee Weapons'),
        ('Travel Supplies', 'Travel Supplies'),
        ('Armor Parts', 'Armor Parts'),
        ('Shields', 'Shields'),
        ('Parrying Weapons', 'Parrying Weapons'),
        ('Jewelry', 'Jewelry'),
        ('Stationery', 'Stationery'),
        ('Animals', 'Animals'),
        ('Pet Supplies', 'Pet Supplies'),
        ('Weapon Accessories', 'Weapon Accessories'),
        ('Tools', 'Tools')
        # Add more options for item types
    )

    RARITY_CHOICES = (
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Epic', 'Epic'),
        ('Legendary', 'Legendary')
        # Add more options for rarity
    )

    CONDITION_CHOICES = (
        ('New', 'New'),
        ('Used', 'Used'),
        ('Damaged', 'Damaged'),
        ('Rusted', 'Rusted'),
        ('Rotten', 'Rotten')
        # Add more options for condition
    )

    STATUS_CHOICES = (
        ('No Status', 'No Status'),
        ('Magical', 'Magical'),
        ('Karmal', 'Karmal'),
        ('Daemon', 'Daemon')
        # Add more options for status
    )

    item_id = models.AutoField(primary_key=True)
    rulesystem = models.CharField(verbose_name='Rulesystem (*)', max_length=20, choices=SYSTEM_CHOICES, default='')
    language = models.CharField(max_length=20, choices=LANG_CHOICES, default='')
    item_type = models.CharField(max_length=20, choices=ITEM_TYP_CHOICES, default='Weapon')
    weight_percentage = models.IntegerField(default=500, validators=[MaxValueValidator(950)], help_text='500 = 50%')
    name = models.CharField(max_length=255,
                            unique=True,
                            help_text='Specific Item Name like Rusty Dagger, Sweet Bread or Leather Shirt')
    item_category_name = models.CharField(max_length=255,
                                          default='',
                                          help_text='Overall Category like Dagger, Bread or Shirt')
    rarity = models.CharField(max_length=20,
                              choices=RARITY_CHOICES,
                              default='Common')
    max_count = models.IntegerField(validators=[MinValueValidator(1)],
                                    default=1,
                                    help_text='How many can be max found while Looting')
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Used')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='No Status')
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
