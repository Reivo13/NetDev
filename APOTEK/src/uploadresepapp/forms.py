from django import forms
from .models import Resep

class ResepForm(forms.ModelForm):
    class Meta:
        model = Resep
        fields = ['judul', 'gambar', 'deskripsi']
    