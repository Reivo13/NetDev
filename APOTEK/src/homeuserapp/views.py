from django.shortcuts import render
from daftarobat.models import Obat
from django.contrib.auth.views import LoginView

def homeuser_view(request):
    return render(request, 'homeuserapp/homeuser.html')

def homeuser(request):
    obat_list = Obat.objects.all()  # Ambil semua obat
    return render(request, 'homeuser/homeuser.html', {'obat_list': obat_list})

class CustomLoginView(LoginView):
    template_name = 'login.html'