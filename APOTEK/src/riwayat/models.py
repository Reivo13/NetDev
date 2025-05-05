from django.db import models
from django.contrib.auth import get_user_model
from adminapp.models import DataObat
from django.utils.timezone import now
import uuid

User = get_user_model()

class RiwayatPembelian(models.Model):
    invoice_number = models.CharField(max_length=100, unique=True, editable=False)
    pembeli = models.ForeignKey(User, on_delete=models.CASCADE)
    kontak_pembeli = models.CharField(max_length=100)
    nama_obat = models.CharField(max_length=120)
    harga_obat = models.PositiveIntegerField()
    jumlah_beli = models.PositiveIntegerField()
    total_harga = models.PositiveIntegerField()
    tanggal_beli = models.DateTimeField(default=now)
    tanggal_bayar = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = f"INV-{uuid.uuid4().hex[:8].upper()}"
        self.total_harga = self.harga_obat * self.jumlah_beli
        super().save(*args, **kwargs)

    def foto_obat(self):
        try:
            obat = DataObat.objects.get(nama_obat=self.nama_obat)
            return obat.foto.url if obat.foto else None
        except DataObat.DoesNotExist:
            return None
    
    def dosis_aturan_pakai(self):
        try:
            obat = DataObat.objects.get(nama_obat=self.nama_obat)
            return obat.dosis_aturan_pakai
        except DataObat.DoesNotExist:
            return "Tidak tersedia"

    def __str__(self):
        return f"{self.invoice_number} - {self.pembeli.username}"
