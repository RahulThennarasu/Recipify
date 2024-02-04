# Generated by Django 4.0.5 on 2022-12-16 04:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_category_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='listingWatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]