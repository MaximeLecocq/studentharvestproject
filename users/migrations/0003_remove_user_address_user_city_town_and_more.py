# Generated by Django 5.0.6 on 2024-08-20 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='user',
            name='city_town',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City/Town'),
        ),
        migrations.AddField(
            model_name='user',
            name='street_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Street Number and Name'),
        ),
    ]
