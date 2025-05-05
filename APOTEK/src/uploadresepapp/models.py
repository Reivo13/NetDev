from django.db import models

class Resep(models.Model):
    judul = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='resep_images/')
    deskripsi = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
    