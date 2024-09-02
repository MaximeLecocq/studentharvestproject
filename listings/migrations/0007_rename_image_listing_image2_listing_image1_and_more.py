# Generated by Django 5.0.6 on 2024-08-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_rename_address_listing_street_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='image',
            new_name='image2',
        ),
        migrations.AddField(
            model_name='listing',
            name='image1',
            field=models.ImageField(default='images/listings/placeholder.jpg', upload_to='images/listings/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/listings/'),
        ),
    ]
