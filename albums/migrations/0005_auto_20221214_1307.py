# Generated by Django 3.2.16 on 2022-12-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singers', '0002_remove_singer_slug'),
        ('albums', '0004_alter_album_released_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='released_by',
        ),
        migrations.AddField(
            model_name='album',
            name='released_by',
            field=models.ManyToManyField(blank=True, to='singers.Singer'),
        ),
    ]
