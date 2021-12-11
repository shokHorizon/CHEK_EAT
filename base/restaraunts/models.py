from django.db import models
from django.contrib.auth.models import User


class Restaraunt(models.Model):
    id = models.UUIDField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    description = models.TextField()
    address = models.CharField(max_length=80)
    phone = models.IntegerField()
    work_time = models.SmallIntegerField()
    close_time = models.SmallIntegerField()
    book_every = models.SmallIntegerField()


class TableType(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=40)
    amount = models.SmallIntegerField()
    restaraunt = models.ForeignKey(Restaraunt, on_delete=models.CASCADE)


class Table(models.Model):
    id = models.UUIDField(primary_key=True)
    bookedTime = models.BigIntegerField()
    tableType = models.ForeignKey(TableType, on_delete=models.CASCADE)


class MenuCategory(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=40)
    desc = models.TextField()
    restaraunt = models.ForeignKey(Restaraunt, on_delete=models.CASCADE)


class Dish(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=40)
    desc = models.TextField()
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
