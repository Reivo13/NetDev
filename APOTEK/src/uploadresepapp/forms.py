from django import forms
from .models import Resep

class ResepForm(forms.ModelForm):
    class Meta:
        model = Resep
        fields = ['judul', 'gambar', 'deskripsi']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Lengkap'}),
            'telepon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nomor Telepon'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'catatan': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Keluhan', 'rows': 5}),
            'foto_resep': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }