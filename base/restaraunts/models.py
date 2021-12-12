from django.db import models
from django.contrib.auth.models import User


class Restaraunt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    phone = models.IntegerField()
    open_time = models.SmallIntegerField()
    close_time = models.SmallIntegerField()
    book_every = models.SmallIntegerField(default=30)


class TableType(models.Model):
    name = models.CharField(max_length=40)
    persons = models.SmallIntegerField()
    restaurant = models.ForeignKey(Restaraunt, on_delete=models.CASCADE)


class Table(models.Model):
    bookedTime = models.BigIntegerField()
    tableType = models.ForeignKey(TableType, on_delete=models.CASCADE)


class MenuCategory(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField()
    restaraunt = models.ForeignKey(Restaraunt, on_delete=models.CASCADE)


class Dish(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    desc = models.TextField()
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
