# Generated by Django 3.2.16 on 2022-12-14 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('singers', '0002_remove_singer_slug'),
        ('albums', '0003_alter_album_released_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='released_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='singers.singer'),
        ),
    ]
