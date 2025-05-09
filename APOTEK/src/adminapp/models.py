from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.exceptions import ValidationError
from .utils import unique_slug_generator

User = get_user_model()

class DataObat(models.Model):
    JENIS_OBAT_CHOICES = [
        ('kapsul', 'Kapsul'),
        ('salep', 'Salep'),
        ('sirup', 'Sirup'),
        ('tablet', 'Tablet'),
    ]

    nama_obat = models.CharField(max_length=120, null=False, blank=False)
    foto = models.ImageField(upload_to='obat_images/', null=False, blank=False)
    jenis_obat = models.CharField(max_length=10, choices=JENIS_OBAT_CHOICES, null=False, blank=False)
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField()
    dosis_aturan_pakai = models.TextField(null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.nama_obat
    
    @property
    def title(self):
        return self.nama_obat
    
    def get_absolute_url(self):
        return reverse('adminapp:detail', kwargs={'slug': self.slug})

class Transaksi(models.Model):
    obat = models.ForeignKey(DataObat, on_delete=models.CASCADE, related_name='transaksi')
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null=True,  # Izinkan null sementara
        blank=True  # Izinkan kosong di form
    )
    jumlah = models.PositiveIntegerField()
    tanggal = models.DateTimeField(auto_now_add=True)
    total_harga = models.PositiveIntegerField(default=0, editable=False)
    
    def clean(self):
        # Validasi sebelum menyimpan
        if self.jumlah <= 0:
            raise ValidationError("Jumlah harus lebih dari 0")
        
        if self.obat.stok < self.jumlah:
            raise ValidationError(f"Stok tidak mencukupi. Stok tersedia: {self.obat.stok}")
    
    def save(self, *args, **kwargs):
        # Hitung total harga
        self.total_harga = self.obat.harga * self.jumlah
        
        # Validasi stok
        self.clean()
        
        # Kurangi stok dengan F() untuk menghindari race condition
        DataObat.objects.filter(pk=self.obat.pk).update(
            stok=models.F('stok') - self.jumlah
        )
        
        # Refresh stok dari database
        self.obat.refresh_from_db()
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.username} - {self.obat.nama_obat} ({self.jumlah})"

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=DataObat)