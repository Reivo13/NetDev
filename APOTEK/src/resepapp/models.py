from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ResepDokter(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    foto_resep  = models.ImageField(upload_to='resep_images/')
    nama_pasien = models.CharField(max_length=100,null=True)
    tanggal_upload = models.DateTimeField(auto_now_add=True)
    dokter      = models.CharField(max_length=100,null=True)  
    tanggal     = models.DateField(null=True,blank= True)  
    obat        = models.CharField(max_length=255,null=True,blank= True)  
    catatan     = models.TextField(null=True,blank= True) 
    slug        = models.SlugField(null=True,blank= True, unique=True)

    def __str__(self):
        return f"Resep oleh {self.user.username}"
