from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=20)
    element = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    mode = models.IntegerField()


class Property(models.Model):
    name = models.ForeignKey(Character, on_delete=models.CASCADE)
    Lv = models.IntegerField()
    baseHP = models.FloatField()
    baseATK = models.FloatField()
    baseDEF = models.FloatField()


class Weapon(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=20)
    baseATK = models.FloatField()
