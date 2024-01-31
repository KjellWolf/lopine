import random
from lopine_items_app.models import Item, ItemRarity, Language, Rulesystem, ItemType, ItemPlace, ItemCondition, \
    ItemStatus


def generate_random_item():
    random_item = Item()

    # Set random values for attributes
    random_item.rulesystem = Rulesystem.objects.order_by('?').first()
    random_item.language = Language.objects.order_by('?').first()
    random_item.item_type = ItemType.objects.order_by('?').first()
    random_item.item_place = ItemPlace.objects.order_by('?').first()
    random_item.weight_percentage = random.randint(1, 1000)
    random_item.name = "Random Item"  # Change this as per the logic for name generation
    random_item.rarity = ItemRarity.objects.order_by('?').first()
    random_item.max_count = random.randint(1, 100)
    random_item.condition = ItemCondition.objects.order_by('?').first()
    random_item.status = ItemStatus.objects.order_by('?').first()
    random_item.status_note = "Random Status Note"  # Change this as per the logic for status note generation
    random_item.weight_gram = random.randint(1, 500)
    random_item.price_gold = random.uniform(0, 1000)

    random_item.save()  # Save generated item to DB
    return random_item