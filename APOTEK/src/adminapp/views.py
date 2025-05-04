from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import DataObat
from .forms import DataObatCreateForm  

class DataObatListView(LoginRequiredMixin, ListView):
     model = DataObat
     template_name = 'adminapp/detail.html'
     login_url = "/login/"
     def get_queryset(self):
        return DataObat.objects.filter(owner=self.request.user)

class DataObatDetailView(LoginRequiredMixin, DetailView):
     model = DataObat
     template_name = 'adminapp/detail.html'
     login_url = "/login/"
     
     def get_queryset(self):
        return DataObat.objects.filter(owner=self.request.user)

class DataObatCreateView(LoginRequiredMixin, CreateView):
    form_class = DataObatCreateForm
    template_name = 'adminapp/form.html'
    login_url = "/login/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return super(DataObatCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Tambah Data Obat"
        return context

class DataObatUpdateView(LoginRequiredMixin, UpdateView):
    model = DataObat
    form_class = DataObatCreateForm
    template_name = 'adminapp/detail-update.html'
    login_url = "/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        name = self.get_object().nama_obat
        context['title'] = f"Update Obat: {name}"
        return context

    def get_queryset(self):
        return DataObat.objects.filter(owner=self.request.user)