# Generated by Django 3.2.16 on 2022-12-14 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('singers', '0002_remove_singer_slug'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='released_by',
        ),
        migrations.AddField(
            model_name='album',
            name='released_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='singers.singer'),
            preserve_default=False,
        ),
    ]
