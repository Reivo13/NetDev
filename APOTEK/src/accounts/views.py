from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

class CustomLoginView(LoginView):
    template_name = 'login.html'

def landing_page(request):
    return render(request, 'landing_page.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Cek kecocokan password
        if password1 != password2:
            messages.error(request, 'Password tidak cocok.')
            return render(request, 'register.html', {
                'username': username,
                'email': email
            })

        # Cek username sudah ada
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah digunakan.')
            return render(request, 'register.html', {
                'email': email
            })

        # Cek email sudah ada
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email sudah digunakan.')
            return render(request, 'register.html', {
                'username': username
            })

        # Buat user baru
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Registrasi berhasil! Silakan login.')
        return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    # Clear existing messages to prevent duplicates
    storage = messages.get_messages(request)
    for _ in storage:
        pass
    storage.used = True

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Selamat datang, {user.username}!')
            return redirect('landing_page')
        else:
            messages.error(request, 'Username atau password salah.')
    
    return render(request, 'login.html')

