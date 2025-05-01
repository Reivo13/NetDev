from django.shortcuts import render
from .models import Obat

def daftar_obat(request):
    query = request.GET.get("search", "").strip()
    filter_kategori = request.GET.get("kategori", "").strip()

    # Ambil semua data obat
    obat_list = Obat.objects.all()

    # Filter berdasarkan pencarian nama obat
    if query:
        obat_list = obat_list.filter(nama__icontains=query)

    # Filter berdasarkan kategori (jenis obat)
    if filter_kategori:
        obat_list = obat_list.filter(kategori=filter_kategori)

    # Kirim data ke template
    return render(request, "daftarobat/daftar_obat.html", {
        "obat_list": obat_list,
        "query": query,
        "filter_kategori": filter_kategori,
    })
