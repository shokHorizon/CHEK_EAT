# Generated by Django 4.0 on 2021-12-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaraunts', '0004_alter_restaraunt_book_every'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabletype',
            old_name='restaraunt',
            new_name='restaurant',
        ),
        migrations.AlterField(
            model_name='restaraunt',
            name='book_every',
            field=models.SmallIntegerField(default=30),
        ),
    ]