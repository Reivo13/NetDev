from django.db import models
from django.db.models.signals import post_save, pre_save
from .utils import unique_slug_generator
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class DataObat(models.Model):
    JENIS_OBAT_CHOICES = [
        ('kapsul', 'Kapsul'),
        ('salep', 'Salep'),
        ('sirup', 'Sirup'),
        ('tablet', 'Tablet'),
    ]
    
    nama_obat   = models.CharField(max_length=120, null= False , blank=False)
    foto        = models.ImageField(upload_to='obat_images/', null= False, blank=False)
    jenis_obat  = models.CharField(max_length=10, choices=JENIS_OBAT_CHOICES,null= False, blank=False)
    harga       = models.PositiveIntegerField() 
    stok        = models.PositiveIntegerField() 
    dosis_aturan_pakai = models.TextField(null= False , blank=False)  
    owner       = models.ForeignKey(User,on_delete=models.CASCADE,null=True)  
    slug        = models.SlugField(null=True,blank= True, unique=True)
    
    def __str__(self):
        return self.nama_obat
    
    @property
    def title(self):
        return self.nama_obat
    
    def get_absolute_url(self):
        return reverse('adminapp:detail', kwargs={'slug': self.slug})
    

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

#def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
    #print('saved')
    #print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver, sender=DataObat)
#post_save.connect(rl_post_save_receiver, sender=DataObat)