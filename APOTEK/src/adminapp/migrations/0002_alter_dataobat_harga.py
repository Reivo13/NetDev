# Generated by Django 4.1.13 on 2025-03-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataobat',
            name='harga',
            field=models.PositiveIntegerField(),
        ),
    ]
