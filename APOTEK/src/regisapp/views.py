from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrasi berhasil! Silakan login.')
            return redirect('loginapp:login')  # arahkan ke halaman login
    else:
        form = RegisterForm()
    return render(request, 'regisapp/regi.html', {'form': form})
