# Generated by Django 5.2 on 2025-05-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riwayat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembelian',
            name='gambar',
            field=models.ImageField(default='assets/obat.png', upload_to='pembelian/'),
        ),
    ]
