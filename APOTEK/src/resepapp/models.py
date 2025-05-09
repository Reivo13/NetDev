
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, pre_save
from .utils import unique_slug_generator
from django.urls import reverse


User = get_user_model()

class ResepDokter(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    nama        = models.CharField(max_length=100,null=True)
    telepon = models.PositiveIntegerField(null=True)
    email       = models.EmailField(max_length=100,null=True)
    foto_resep  = models.ImageField(upload_to='resep_images/')
    catatan     = models.TextField(null=True,blank= True) 
    slug        = models.SlugField(null=True,blank= True, unique=True)


    def __str__(self):
        return f"Resep oleh {self.user.username}"
    
    @property
    def title(self):
        return self.user
    
    def get_absolute_url(self):
        return reverse('resep:detail', kwargs={'slug': self.slug})


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    #def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
        #print('saved')
        #print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver, sender=ResepDokter)
        #post_save.connect(rl_post_save_receiver, sender=DataObat)