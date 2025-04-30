from django.db import models
from daftarobat.models import Obat

class HistoryPembelian(models.Model):
    obat = models.ForeignKey(Obat, on_delete=models.SET_NULL, null=True)
    nama_pembeli = models.CharField(max_length=100)
    tanggal_pembelian = models.DateTimeField(auto_now_add=True)
    jumlah = models.PositiveIntegerField()

    def __str__(self):
        return f"Pembelian {self.nama_obat} oleh {self.nama_pembeli}"

    @property
    def nama_obat(self):
        return self.obat.nama if self.obat else '-'

    @property
    def gambar(self):
        return self.obat.gambar if self.obat else None

    @property
    def harga_satuan(self):
        return self.obat.harga if self.obat else 0

    @property
    def cara_pakai(self):
        return self.obat.cara_pemakaian if self.obat else '-'

    @property
    def total_harga(self):
        return self.jumlah * self.harga_satuan
