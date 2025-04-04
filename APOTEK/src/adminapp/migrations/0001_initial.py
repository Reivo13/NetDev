# Generated by Django 4.1.13 on 2025-03-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataObat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_obat', models.CharField(max_length=120)),
                ('jenis_obat', models.CharField(choices=[('kapsul', 'Kapsul'), ('salep', 'Salep'), ('sirup', 'Sirup'), ('tablet', 'Tablet')], max_length=10)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=12)),
                ('stok', models.PositiveIntegerField()),
                ('dosis_aturan_pakai', models.TextField()),
            ],
        ),
    ]
