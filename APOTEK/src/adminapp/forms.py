from django import forms
from .models import DataObat

class DataObatCreateForm(forms.ModelForm):
    class Meta:
        model = DataObat
        fields = ['nama_obat',
                  'foto',
                  'jenis_obat', 
                  'harga', 
                  'stok', 
                  'dosis_aturan_pakai',]
        widgets = {
            'nama_obat': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'jenis_obat': forms.Select(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),
            'dosis_aturan_pakai': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }