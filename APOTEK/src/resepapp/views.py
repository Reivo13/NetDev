from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import ResepDokter
from django.urls import reverse_lazy

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
