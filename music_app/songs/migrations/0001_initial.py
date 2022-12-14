# Generated by Django 3.2.16 on 2022-12-14 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('singers', '0002_remove_singer_slug'),
        ('albums', '0008_alter_album_released_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('in_the_album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='albums.album')),
                ('released_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='singers.singer')),
            ],
        ),
    ]