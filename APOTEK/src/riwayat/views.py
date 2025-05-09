from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RiwayatPembelian

class RiwayatPembelianView(LoginRequiredMixin, ListView):
    model = RiwayatPembelian
    template_name = 'riwayat_pembelian.html'
    context_object_name = 'riwayat_list'

    def get_queryset(self):
        return RiwayatPembelian.objects.filter(pembeli=self.request.user).order_by('-tanggal_bayar')
