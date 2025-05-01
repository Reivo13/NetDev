from django.shortcuts import render, redirect
from .forms import ResepForm
from .models import Resep

def upload_resep(request):
    if request.method == 'POST':
        form = ResepForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadresepapp:daftar')
    else:
        form = ResepForm()
    return render(request, 'uploadresepapp/upload_form.html', {'form': form})

def daftar_resep(request):
    resep_list = Resep.objects.all().order_by('-uploaded_at')
    return render(request, 'uploadresepapp/upload_list.html', {'resep_list': resep_list})
