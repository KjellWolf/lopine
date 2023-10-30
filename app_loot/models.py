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
        ('Weapon', 'Weapon'),
        ('Armor', 'Armor'),
        ('Household', 'Household'),
        ('Nature_Material', 'Nature_Material')
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
    rulesystem = models.CharField(max_length=20, choices=SYSTEM_CHOICES, default='')
    language = models.CharField(max_length=20, choices=LANG_CHOICES, default='')
    item_type = models.CharField(max_length=20, choices=ITEM_TYP_CHOICES, default='Weapon')
    weight_percentage = models.IntegerField(default=500, validators=[MaxValueValidator(950)])
    name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=255, default='')
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES, default='Common')
    max_count = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Used')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='No Status')
    status_note = models.CharField(max_length=255, default='None')
    weight_gram = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    price_gold = models.FloatField(default=1, validators=[MinValueValidator(0)])




