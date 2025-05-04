from django.shortcuts import render
from .models import Pembelian

def riwayat(request):
    data = Pembelian.objects.prefetch_related('invoices').all()

    riwayat = []
    for pembelian in data:
        invoice = pembelian.invoices.first()
        if invoice:
            riwayat.append({
                'pembelian': pembelian,
                'invoice': invoice,
            })

    return render(request, 'riwayat_pembelian.html', {'riwayat': riwayat})

def faq(request):
    return render(request, 'footer/template/faq/faq.html')

def syarat(request):
    return render(request, 'footer/template/S&K/syarat.html')

def kebijakan(request):
    return render(request, 'footer/template/privasi/kebijakan.html')

