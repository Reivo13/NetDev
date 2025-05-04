from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from adminapp.models import DataObat, Transaksi  # Impor dari adminapp
from django.core.exceptions import ValidationError

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