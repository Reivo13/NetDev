import uuid
from django.db import models
from django.utils import timezone


class Pembelian(models.Model):
    gambar = models.ImageField(upload_to='pembelian/', default='assets/obat.png')
    nama_obat = models.CharField(max_length=100)
    harga = models.PositiveIntegerField()
    keterangan = models.TextField()
    jumlah = models.PositiveIntegerField()

    @property
    def total(self):
        return self.harga * self.jumlah

    def __str__(self):
        return f"{self.nama_obat} x {self.jumlah}"


class Invoice(models.Model):
    pembelian = models.ForeignKey(Pembelian, on_delete=models.CASCADE, related_name='invoices')
    nama_pemesan = models.CharField(max_length=100)
    kontak_pemesan = models.CharField(max_length=20)
    invoice_number = models.CharField(max_length=20, unique=True, editable=False)
    waktu_beli = models.DateTimeField(default=timezone.now)
    waktu_bayar = models.DateTimeField()

    total_amount = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Auto-generate invoice number once
        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()
        if not self.total_amount:
            self.total_amount = self.pembelian.total
        super().save(*args, **kwargs)

    def generate_invoice_number(self):
        return f"INV-{uuid.uuid4().hex[:10].upper()}"

    def __str__(self):
        return f"Invoice {self.invoice_number}"


class ItemInvoice(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    @property
    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.item_name} ({self.quantity}x)"
