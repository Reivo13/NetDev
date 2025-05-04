from django.db import models

class Obat(models.Model):
    KATEGORI_CHOICES = [
        ("Tablet", "Tablet"),
        ("Kapsul", "Kapsul"),
        ("Sirup", "Sirup"),
        ("Salep", "Salep"),
    ]

    nama = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='')
    stok = models.PositiveIntegerField()
    cara_pemakaian = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)

    def __str__(self):
        return self.nama
