# Generated by Django 4.2.3 on 2023-07-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='artist',
        ),
        migrations.AddField(
            model_name='band',
            name='artists',
            field=models.ManyToManyField(to='core.artist'),
        ),
    ]
