from django.db import models

class DataObat(models.Model):
    JENIS_OBAT_CHOICES = [
        ('kapsul', 'Kapsul'),
        ('salep', 'Salep'),
        ('sirup', 'Sirup'),
        ('tablet', 'Tablet'),
    ]
    
    nama_obat = models.CharField(max_length=120)
    jenis_obat = models.CharField(max_length=10, choices=JENIS_OBAT_CHOICES)
    harga = models.DecimalField(max_digits=12, decimal_places=2)  # Untuk menyimpan harga dalam format Rupiah
    stok = models.PositiveIntegerField()  # Hanya menerima angka positif
    dosis_aturan_pakai = models.TextField()  # Untuk teks panjang

    def __str__(self):
        return self.nama_obat