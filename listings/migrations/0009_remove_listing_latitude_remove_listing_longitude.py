# Generated by Django 5.0.6 on 2024-08-21 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_listing_latitude_listing_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='longitude',
        ),
    ]
