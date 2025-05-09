from django.shortcuts import render

from adminapp.models import DataObat

def landing_page(request):
    jenis_filter = request.GET.get('jenis', None)
    if jenis_filter:
        obat_list = DataObat.objects.filter(jenis_obat=jenis_filter)
    else:
        obat_list = DataObat.objects.all()
    return render(request, 'pages/landing_page.html', {'obat_list': obat_list, 'jenis_filter': jenis_filter})

from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from adminapp.models import DataObat, Transaksi  # Impor dari adminapp
from django.core.exceptions import ValidationError
from riwayat.models import RiwayatPembelian 

class LandingPageView(ListView):
    model = DataObat
    template_name = 'pages/landing_page.html'
    context_object_name = 'obat_list'

@login_required
def beli_obat(request, obat_id):
    try:
        obat = DataObat.objects.get(pk=obat_id)
        jumlah = int(request.POST.get('jumlah', 1))
        
        # Buat transaksi (validasi otomatis di model)
        transaksi = Transaksi(
            obat=obat,
            user=request.user,
            jumlah=jumlah
        )
        transaksi.save()
        
        RiwayatPembelian.objects.create(
            pembeli=request.user,
            kontak_pembeli=request.user.email,  # atau ganti dengan profil/kontak user lainnya
            nama_obat=obat.nama_obat,
            harga_obat=obat.harga,
            jumlah_beli=jumlah,
            total_harga=obat.harga * jumlah,
        )
        
        return JsonResponse({
            'status': 'success',
            'stok_terbaru': obat.stok,
            'message': 'Pembelian berhasil',
            'total_harga': transaksi.total_harga
        })
        
    except DataObat.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Obat tidak ditemukan'
        }, status=404)
        
    except ValidationError as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
