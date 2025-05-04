from django import forms
from .models import ResepDokter

class ResepDokterCreateForm(forms.ModelForm):
     class Meta:
        model = ResepDokter
        fields = ['user', 'nama', 'telepon', 'email', 'catatan', 'foto_resep']
        widgets = {
            'user': forms.HiddenInput(),  # Agar tidak tampil di form, tapi bisa di-set di view
        }