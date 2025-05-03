from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import JsonResponse
from adminapp.models import DataObat, Transaksi

class LandingPageView(ListView):
    model = DataObat
    template_name = 'pages/landing_page.html'
    context_object_name = 'obat_list'
    paginate_by = 12

    def get_queryset(self):
        # Tambahkan filter/search jika diperlukan
        return DataObat.objects.all()

@login_required
def beli_obat(request, obat_id):
    obat = get_object_or_404(DataObat, id=obat_id)
    
    if request.method == 'POST':
        if obat.stok > 0:
            obat.stok -= 1
            obat.save()
            
            Transaksi.objects.create(
                user=request.user,
                obat=obat,
                jumlah=1,
                total_harga=obat.harga
            )
            
            return JsonResponse({
                'success': True,
                'new_stock': obat.stok,
                'obat_id': obat.id
            })
    
    return JsonResponse({'success': False, 'message': 'Metode tidak valid atau stok habis'})
