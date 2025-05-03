from django.shortcuts import render, redirect
from .forms import ResepForm
from .models import Resep

from django.views.generic import DeleteView ,ListView, DetailView, CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from resepapp.models import ResepDokter
from django.shortcuts import render
from resepapp.forms import ResepDokterCreateForm
from django.shortcuts import render

class ResepCreateView(LoginRequiredMixin, CreateView):
    model = ResepDokter
    fields = ['nama', 'telepon', 'email', 'foto_resep', 'catatan']
    template_name = 'uploadresepapp/index.html'
    success_url = reverse_lazy('homeuserapp:homeuser')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Otomatis isi user
        messages.success(self.request, 'Resep berhasil ditambahkan!')
        return super().form_valid(form)


