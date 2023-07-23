# Generated by Django 4.2.3 on 2023-07-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_genre_band_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.ManyToManyField(blank=True, to='core.genre'),
        ),
    ]
