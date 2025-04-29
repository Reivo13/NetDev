
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, pre_save
from .utils import unique_slug_generator
from django.urls import reverse


User = get_user_model()

class ResepDokter(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    foto_resep  = models.ImageField(upload_to='resep_images/')
    tanggal_upload = models.DateTimeField(auto_now_add=True)
    dokter      = models.CharField(max_length=100,null=True)  
    tanggal     = models.DateField(null=True,blank= True)  
    obat        = models.CharField(max_length=255,null=True,blank= True)  
    catatan     = models.TextField(null=True,blank= True) 
    slug        = models.SlugField(unique=True, blank=True)



    def __str__(self):
        return f"Resep oleh {self.user.username}"
    
    @property
    def title(self):
        return f"Resep oleh {self.user.username}"
    
    def get_absolute_url(self):
        return reverse('resep:detail', kwargs={'slug': self.slug})


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=ResepDokter)
      