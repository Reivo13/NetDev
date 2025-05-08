from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import DataObat
from resepapp.models import ResepDokter
from .forms import DataObatCreateForm 
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect 
from django.contrib import messages 


class StaffRequiredMixin(UserPassesTestMixin):
    login_url = "/login/"

    def test_func(self):
        user = self.request.user
        return user.is_active and (user.is_staff or user.is_superuser)

class DataObatListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = DataObat
    template_name = 'adminapp/admin_dashboard.html'
    login_url = "/login/"


class DataObatDetailView(LoginRequiredMixin, StaffRequiredMixin, DetailView):
    model = DataObat
    template_name = 'adminapp/admin_dashboard.html'
    login_url = "/login/"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, f"Obat '{self.object.nama_obat}' berhasil diupdate.")
        return redirect('adminapp:list')

class DataObatCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    form_class = DataObatCreateForm
    template_name = 'adminapp/form.html'
    login_url = "/login/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('adminapp:list') 
    
    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, f"Obat '{self.object.nama_obat}' berhasil ditambahkan.")
        return redirect('adminapp:list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Tambah Data Obat"
        return context
    

class DataObatUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = DataObat
    form_class = DataObatCreateForm
    template_name = 'adminapp/detail-update.html'
    login_url = "/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        name = self.get_object().nama_obat
        context['title'] = f"Update Obat: {name}"
        return context

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, f"Obat '{self.object.nama_obat}' berhasil diupdate.")
        return redirect('adminapp:list')


class DataObatDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = DataObat
    template_name = 'adminapp/obat_delete.html'
    success_url = reverse_lazy('adminapp:list')
    login_url = "/login/"


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        nama_obat = self.object.nama_obat 
        messages.success(request, f"Obat '{nama_obat}' berhasil dihapus.")
        print(f"Obat '{nama_obat}' berhasil dihapus.") 
        return super().delete(request, *args, **kwargs)
    

class DashboardView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'adminapp/admin_dashboard.html'
    login_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obat_list'] = DataObat.objects.all()
        context['resep_list'] = ResepDokter.objects.all()
        return context