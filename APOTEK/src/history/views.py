from django.shortcuts import render
from .models import HistoryPembelian

def history_index(request):
    pembelian = HistoryPembelian.objects.all().order_by('-tanggal_pembelian')
    return render(request, 'history/history.html', {'pembelian': pembelian})