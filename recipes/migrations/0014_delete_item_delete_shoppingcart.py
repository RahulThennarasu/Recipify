# Generated by Django 4.0.5 on 2022-12-21 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
    ]
