# Generated by Django 4.0.5 on 2022-12-18 01:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='buy',
            field=models.ManyToManyField(blank=True, null=True, related_name='listingBuy', to=settings.AUTH_USER_MODEL),
        ),
    ]
