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
                  'dosis_aturan_pakai']