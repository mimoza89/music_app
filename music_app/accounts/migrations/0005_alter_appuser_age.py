# Generated by Django 3.2.16 on 2022-12-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_appuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]