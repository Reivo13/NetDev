# Generated by Django 4.2.20 on 2025-04-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_dataobat_harga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataobat',
            name='harga',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
