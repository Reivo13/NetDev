from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ResepDokter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foto_resep = models.ImageField(upload_to='resep_images/')
    tanggal_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resep oleh {self.user.username}"
