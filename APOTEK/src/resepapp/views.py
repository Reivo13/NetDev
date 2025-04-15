
from django.views.generic import DeleteView ,ListView, DetailView, CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ResepDokter

class ResepListView(ListView):
    model = ResepDokter
    template_name = 'resepdokter_list.html'

class ResepDetailView(DetailView):
    model = ResepDokter
    template_name = 'resepdokter_detail.html'

class ResepCreateView(CreateView):
    model = ResepDokter
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('resepapp:list')

class ResepUpdateView(UpdateView):
    model = ResepDokter
    fields = '__all__'
    template_name = 'resepapp/detail_update.html'
    success_url = reverse_lazy('resepapp:list')

class ResepDeleteView(LoginRequiredMixin, DeleteView):
    model = ResepDokter
    template_name = 'resepapp/resep_delete.html'  # Buat template ini
    success_url = reverse_lazy('adminapp:list')   # Redirect ke daftar resep
    login_url = "/login/"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        nama_pasien = self.object.nama_pasien
        messages.success(request, f"Resep untuk pasien '{nama_pasien}' berhasil dihapus.")
        return super().delete(request, *args, **kwargs)