from django.shortcuts import render, redirect
from daftarobat.models import Obat
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from daftarobat.models import Obat
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def homeuser_view(request):
    return redirect('landing_page:landing_page')

def homeuser(request):
    obat_list = Obat.objects.all()  # Ambil semua obat
    return render(request, 'homeuser/landing_page.html', {'obat_list': obat_list})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            messages.error(request, 'Email tidak ditemukan.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Selamat datang, {user.username}!')
            return redirect('home')  # Ganti 'home' dengan halaman utama aplikasi Anda
        else:
            messages.error(request, 'Password salah.')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username sudah digunakan.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email sudah digunakan.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Registrasi berhasil! Silakan login.')
                return redirect('login')
        else:
            messages.error(request, 'Password tidak cocok.')

    return render(request, 'register.html')

def homeuser(request):
    obat_list = Obat.objects.all()  # Ambil semua obat
    return render(request, 'homeuser/homeuser.html', {'obat_list': obat_list})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            messages.error(request, 'Email tidak ditemukan.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Selamat datang, {user.username}!')
            return redirect('home')  # Ganti 'home' dengan halaman utama aplikasi Anda
        else:
            messages.error(request, 'Password salah.')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username sudah digunakan.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email sudah digunakan.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Registrasi berhasil! Silakan login.')
                return redirect('login')
        else:
            messages.error(request, 'Password tidak cocok.')

    return render(request, 'register.html')