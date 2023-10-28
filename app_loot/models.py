from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
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
        # Weitere Optionen für Item-Typen hinzufügen
    )

    RARITY_CHOICES = (
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Epic', 'Epic'),
        ('Legendary', 'Legendary'),
        # Weitere Optionen für Rarität hinzufügen
    )

    CONDITION_CHOICES = (
        ('New', 'New'),
        ('Used', 'Used'),
        ('Damaged', 'Damaged'),
        ('Rusted', 'Rusted'),
        ('Rotten', 'Rotten')
        # Weitere Optionen für Zustand hinzufügen
    )

    STATUS_CHOICES = (
        ('No Status', 'No_Status'),
        ('Magical', 'Magical'),
        ('Karmal', 'Karmal'),
        # Weitere Optionen für Status hinzufügen
    )

    item_id = models.AutoField(primary_key=True)
    rulesystem = models.CharField(name='Rulesystem (*)', max_length=20, choices=SYSTEM_CHOICES, default='')
    item_typ = models.CharField(max_length=20, choices=ITEM_TYP_CHOICES, default='Weapon')
    gewichtung = models.IntegerField(default=1000)
    name = models.CharField(name='Name (*)', max_length=255)
    common_name = models.CharField(name='Common Name (*)', max_length=255, default='')
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES, default='Common')
    max_count = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    material = models.CharField(name='Material (*)', max_length=255)
    color = models.CharField(name='Color (*)', max_length=255)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Used')
    status = models.CharField(name='Status (*)', max_length=20, choices=STATUS_CHOICES, default='No_Status')
    status_note = models.CharField(name='Status Note', max_length=255, default='None')
    weight = models.IntegerField(name='Weight (gramm)', default=1, validators=[MinValueValidator(1)])




