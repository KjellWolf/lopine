from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    ITEM_TYP_CHOICES = (
        ('Weapon', 'Weapon'),
        ('Armor', 'Armor'),
        ('Household', 'Household'),
        ('Nature_Matrial', 'Nature_Matrial')
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
        # Weitere Optionen für Zustand hinzufügen
    )

    STATUS_CHOICES = (
        ('No Status', 'No_Status'),
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        # Weitere Optionen für Status hinzufügen
    )

    item_id = models.AutoField(primary_key=True)
    item_typ = models.CharField(max_length=20, choices=ITEM_TYP_CHOICES, default='Common Item')
    gewichtung = models.IntegerField(default=1000)
    name = models.CharField(max_length=255)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES, default='Common')
    max_count = models.IntegerField(validators=[MinValueValidator(0)])
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Used')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Unremarkable')
    weight = models.IntegerField(default='0', validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class ItemDetails(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='details')

    # Hier können Sie zusätzliche Felder für die Details des Items hinzufügen, die nur für bestimmte Item-Instanzen gelten.

    def __str__(self):
        return f"Details for {self.item.Name}"
