

# Create your views here.
from django.shortcuts import render

def rincian(request):
    return render(request, 'rincian_obat.html')