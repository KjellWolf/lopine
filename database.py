from django.db import models


class ItemRarity(models.Model):
    rarity = models.CharField(max_length=30)


class ItemMaterial(models.Model):
    material = models.CharField(max_length=30)


class ItemCondition(models.Model):
    condition = models.CharField(max_length=30)


class ItemState(models.Model):
    state = models.CharField(max_length=30)


class ItemWeights(models.Model):
    weights = models.IntegerField(max_length=1000)
    rarity = models.ForeignKey(on_delete=models.CASCADE)


class Items(models.Model):
    item_name = models.CharField(max_length=30)
    item_weights = models.ForeignKey(ItemWeights.weights, on_delete=models.CASCADE)
    item_rarity = models.ForeignKey(ItemWeights.rarity,on_delete=models.CASCADE())
    item_count = models.IntegerField()
    item_material = models.ForeignKey(ItemMaterial, on_delete=models.CASCADE)
    item_condition = models.ForeignKey(ItemCondition, on_delete=models.CASCADE)
    item_state = models.ForeignKey(ItemState, on_delete=models.CASCADE)


class BegegOrt(models.Model):
    Ort = models.CharField(max_length=40)


class Begegnung(models.Model):
    begeg_ort = models.ForeignKey(BegegOrt, on_delete=models.CASCADE)
    begeg_text = models.CharField(max_length=256)
