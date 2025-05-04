from django import forms
from .models import ResepDokter

class ResepDokterCreateForm(forms.ModelForm):
    class Meta:
        model =ResepDokter
        fields = ['user',
                  'foto_resep',
                  'nama_pasien',
                  'tanggal_upload', 
                  'dokter', 
                  'tanggal', 
                  'obat',
                  'catatan']