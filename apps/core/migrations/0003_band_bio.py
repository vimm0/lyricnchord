# Generated by Django 4.2.3 on 2023-07-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_band_artist_band_artists'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
