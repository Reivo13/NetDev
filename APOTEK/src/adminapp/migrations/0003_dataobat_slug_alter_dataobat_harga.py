# Generated by Django 4.1.13 on 2025-04-02 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_dataobat_harga'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataobat',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataobat',
            name='harga',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
