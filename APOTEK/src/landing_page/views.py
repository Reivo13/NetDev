from django.shortcuts import redirect, render, get_object_or_404
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

def beli_obat(request, obat_id):
    if request.method == 'POST':
        obat = get_object_or_404(DataObat, pk=obat_id)
        jumlah = int(request.POST.get('jumlah', 1))
        
        if obat.stok >= jumlah:
            Transaksi.objects.create(obat=obat, jumlah=jumlah)
            return redirect('daftar_obat')
        else:
            return HttpResponse("Stok tidak mencukupi", status=400)
    return redirect('daftar_obat')
