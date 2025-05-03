
from django.views.generic import DeleteView ,ListView, DetailView, CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ResepDokter
from django.shortcuts import render

def homeuser_view( request):
    return render(request, 'resepapp/homeuser.html')

class ResepListView( LoginRequiredMixin,ListView):
    model = ResepDokter
    template_name = 'resepdokter_list.html'

class ResepDetailView( LoginRequiredMixin,DetailView):
    model = ResepDokter
    template_name = 'resepdokter_detail.html'

class ResepCreateView(LoginRequiredMixin, CreateView):
    model = ResepDokter
    fields = ['nama', 'telepon', 'email', 'foto_resep', 'catatan']
    template_name = 'resepapp/form.html'
    success_url = reverse_lazy('homeuserapp:homeuser')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Otomatis isi user
        messages.success(self.request, 'Resep berhasil ditambahkan!')
        return super().form_valid(form)


class ResepUpdateView( LoginRequiredMixin,UpdateView):
    model = ResepDokter
    fields = '__all__'
    template_name = 'resepapp/detail_update.html'
    success_url = reverse_lazy('resepapp:list')

class ResepDeleteView(LoginRequiredMixin, DeleteView):
    model = ResepDokter
    template_name = 'resepapp/resep_delete.html'  # Buat template ini
    success_url = reverse_lazy('resepapp:list')   # Redirect ke daftar resep
    login_url = "/login/"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        nama_pasien = self.object.nama_pasien
        messages.success(request, f"Resep untuk pasien '{nama_pasien}' berhasil dihapus.")
        return super().delete(request, *args, **kwargs)
    
